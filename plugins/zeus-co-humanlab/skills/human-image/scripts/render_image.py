#!/usr/bin/env python3
"""
render_image.py — Wrapper Higgsfield CLI para human-image.

Faz upload (se houver referência), gera, baixa, escreve manifest.

Uso:
    python3 render_image.py render <prompt.txt> --aspect-ratio 4:5 --resolution 2k --output-dir <pasta>
    python3 render_image.py render <prompt.txt> --aspect-ratio 4:5 --resolution 2k --output-dir <pasta> --reference /path/ref.png

Requisitos: higgsfield CLI logado, jq, python3.
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime


def run(cmd, capture=True):
    """Roda comando shell e retorna stdout."""
    r = subprocess.run(cmd, shell=True, capture_output=capture, text=True)
    if r.returncode != 0:
        print(f"[ERRO] cmd: {cmd}", file=sys.stderr)
        print(r.stderr, file=sys.stderr)
        sys.exit(r.returncode)
    return r.stdout.strip()


def check_cli():
    """Garante que higgsfield CLI está disponível e logado."""
    try:
        subprocess.run("which higgsfield", shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("[ERRO] Higgsfield CLI não encontrado. Instale e rode `higgsfield auth login`.", file=sys.stderr)
        sys.exit(1)

    status = run("higgsfield account status")
    if "@" not in status:
        print("[ERRO] Higgsfield CLI não logado. Rode `higgsfield auth login`.", file=sys.stderr)
        sys.exit(1)


def upload_reference(ref_path: Path) -> str:
    """Faz upload da referência e devolve o UUID."""
    print(f"[upload] {ref_path}")
    raw = run(f'higgsfield upload create "{ref_path}"')
    try:
        data = json.loads(raw)
        return data.get("uuid") or data.get("id") or raw.strip()
    except json.JSONDecodeError:
        return raw.strip()


def render(prompt: str, aspect: str, resolution: str, ref_uuid: str = None) -> dict:
    """Dispara o render e devolve o payload."""
    base = f'higgsfield generate create nano_banana_2 --prompt "{prompt}" --aspect_ratio "{aspect}" --resolution "{resolution}"'
    if ref_uuid:
        base += f' --image "{ref_uuid}"'
    print(f"[render] aspect={aspect} resolution={resolution} ref={'yes' if ref_uuid else 'no'}")
    raw = run(base)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw": raw}


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("render", help="Render uma imagem")
    r.add_argument("prompt_file", help="Path para prompt.txt")
    r.add_argument("--aspect-ratio", default="4:5", choices=["auto", "1:1", "3:2", "2:3", "4:3", "3:4", "4:5", "5:4", "9:16", "16:9", "21:9"])
    r.add_argument("--resolution", default="2k", choices=["1k", "2k", "4k"])
    r.add_argument("--output-dir", required=True, help="Pasta de output")
    r.add_argument("--reference", help="Path para imagem de referência (opcional)")

    args = p.parse_args()

    if args.cmd == "render":
        check_cli()

        prompt_file = Path(args.prompt_file)
        if not prompt_file.exists():
            print(f"[ERRO] Prompt file não existe: {prompt_file}", file=sys.stderr)
            sys.exit(1)

        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        prompt = prompt_file.read_text().strip()

        ref_uuid = None
        if args.reference:
            ref_path = Path(args.reference)
            if not ref_path.exists():
                print(f"[ERRO] Referência não existe: {ref_path}", file=sys.stderr)
                sys.exit(1)
            ref_uuid = upload_reference(ref_path)

        result = render(prompt, args.aspect_ratio, args.resolution, ref_uuid)

        manifest = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "model": "nano_banana_2",
            "aspect_ratio": args.aspect_ratio,
            "resolution": args.resolution,
            "reference_uuid": ref_uuid,
            "prompt_chars": len(prompt),
            "result": result,
        }
        manifest_path = out_dir / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
        print(f"[manifest] {manifest_path}")
        print(f"[done] Output em {out_dir}")
        print("[next] Baixe a imagem renderizada via Higgsfield (caso CLI não baixe automático)")


if __name__ == "__main__":
    main()
