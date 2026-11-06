"""Estilo de gráficos (matplotlib) y guardado de figuras.

Uso dentro de un notebook:

    from src.plotting import use_style, guardar
    use_style("notes")     # o "slides"
    ...
    guardar(fig, "01-target.png")
"""

from __future__ import annotations

from typing import Any, Dict

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

from src.config import FIG_DIR

# Paleta cualitativa apta para daltonismo (Wong, 2011).
COLORBLIND_CYCLE = [
    "#000000", "#E69F00", "#56B4E9", "#009E73",
    "#F0E442", "#0072B2", "#D55E00", "#CC79A7",
]

# Ajustes por contexto: "notes" para el informe impreso, "slides" para la presentación.
CONTEXTS: Dict[str, Dict[str, Any]] = {
    "notes": {
        "figure.figsize": (5.5, 3.4), "font.size": 10, "axes.titlesize": 11,
        "axes.labelsize": 10, "legend.fontsize": 9, "xtick.labelsize": 9,
        "ytick.labelsize": 9, "lines.linewidth": 1.5, "lines.markersize": 5,
    },
    "slides": {
        "figure.figsize": (7.0, 4.2), "font.size": 14, "axes.titlesize": 16,
        "axes.labelsize": 14, "legend.fontsize": 12, "xtick.labelsize": 12,
        "ytick.labelsize": 12, "lines.linewidth": 2.2, "lines.markersize": 7,
    },
}


def use_style(context: str = "notes") -> Dict[str, Any]:
    """Aplica el estilo de matplotlib para ``context`` ("notes" o "slides")."""
    if context not in CONTEXTS:
        raise ValueError(f"contexto desconocido {context!r}; se esperaba uno de {sorted(CONTEXTS)}")
    params: Dict[str, Any] = {
        "text.usetex": False,
        "font.family": "serif",
        "font.serif": ["CMU Serif", "Computer Modern Roman", "DejaVu Serif",
                       "Times New Roman", "serif"],
        "mathtext.fontset": "cm",
        "axes.grid": True, "grid.alpha": 0.3, "grid.linewidth": 0.6,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.axisbelow": True,
        "axes.prop_cycle": cycler(color=COLORBLIND_CYCLE),
        "figure.constrained_layout.use": True,
        "figure.dpi": 100, "savefig.dpi": 200,
        "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
        "legend.frameon": False,
    }
    params.update(CONTEXTS[context])
    mpl.rcParams.update(params)
    return params


def guardar(fig, nombre: str) -> None:
    """Guarda la figura en ``results/figures/`` y la muestra en el notebook."""
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / nombre)
    plt.show()
