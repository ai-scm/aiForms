#!/usr/bin/env python3
"""
script_magico.py

Lee el archivo .env y renderiza config.yml inyectando las variables de entorno.
Usa Jinja2 para sustituir placeholders del tipo {{ VAR_NAME }}.
"""

import os
import re
from pathlib import Path

# Directorio base (donde está este script)
BASE_DIR = Path(__file__).resolve().parent

ENV_FILE = BASE_DIR / ".env"
CONFIG_TEMPLATE = BASE_DIR / "config.template.yml"
CONFIG_OUTPUT = BASE_DIR / "config.yml"


def load_env(env_path: Path) -> dict[str, str]:
    """Parsea un archivo .env y retorna un diccionario con las variables."""
    env_vars: dict[str, str] = {}
    if not env_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {env_path}")

    with env_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                env_vars[key.strip()] = value.strip()
    return env_vars


def render_config(template_path: Path, output_path: Path, env_vars: dict[str, str]) -> None:
    """
    Lee el template YAML con placeholders {{ VAR }} y los reemplaza
    con los valores del diccionario env_vars.
    """
    if not template_path.exists():
        raise FileNotFoundError(f"No se encontró el template: {template_path}")

    content = template_path.read_text(encoding="utf-8")

    # Patrón para detectar {{ VAR_NAME }}
    pattern = re.compile(r'(?<!\{)\{\s*\{?\s*(\w+)\s*\}?\s*\}(?!\})')

    def replacer(match: re.Match) -> str:
        var_name = match.group(1)
        if var_name in env_vars:
            return env_vars[var_name]
        # Si no existe la variable, dejar el placeholder como advertencia
        print(f"[WARN] Variable '{var_name}' no encontrada en .env")
        return match.group(0)

    rendered = pattern.sub(replacer, content)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"[OK] config.yml generado en: {output_path}")


def main() -> None:
    print("=== Script Mágico: Inyección de Variables ===")

    # 1. Cargar variables desde .env
    env_vars = load_env(ENV_FILE)
    print(f"[INFO] Variables cargadas desde .env: {list(env_vars.keys())}")

    # 2. Exportar al entorno actual (opcional, por si otro proceso lo necesita)
    for key, value in env_vars.items():
        os.environ[key] = value

    # 3. Renderizar config.yml desde el template
    render_config(CONFIG_TEMPLATE, CONFIG_OUTPUT, env_vars)

    print("=== Listo ===")


if __name__ == "__main__":
    main()
