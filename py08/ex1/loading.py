#! /usr/bin/env python3

# ============================== Built-in Import ==============================
#                    Here we import native modules normally
# -----------------------------------------------------------------------------

import sys
from importlib import metadata
from typing import Any


# ================================ Safe Import ================================
#      Here we import external modules, so we use try/except error handling
# -----------------------------------------------------------------------------

try:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    # import tensorflow as tf  # test
except ImportError as e:  # {e} example: "No module named 'pandas'"
    missing_pkg = str(e).split("'")[1] if "'" in str(e) else "unknown"
    pkgs = "numpy pandas matplotlib"

    print(f"❌ [ERROR] Missing dependency: {missing_pkg}")
    print("\n-------- Install using pip --------")
    print(f"pip install {pkgs}\nor")
    print("pip install -r requirements.txt")

    print("\n------ Install using Poetry ------")
    print(f"poetry add {pkgs}\nor")
    print("poetry install")

    sys.exit(1)


# ============================ Packages Validation ============================
#      Function to validate the input packages list showing their metadata
# -----------------------------------------------------------------------------

def validate_pkg(pkg_list: dict[str, str]) -> None:
    is_venv = (sys.base_prefix != sys.prefix)
    if not is_venv:
        print("🚧 You are out of a virtual environment "
              "activate one using:\n"
              "python3 -m venv venv\n or\n"
              "poetry init | poetry install")
        return

    for pkg_key, pkg_str in pkg_list.items():
        has_pkg = metadata.metadata(pkg_key)
        print(f"✅ [OK] {pkg_key} {has_pkg['Version']} - "
              f"{pkg_str}")
    return


# ============================== Matrix Creation ==============================
#          Generate a matrix using numpy, pandas & matplotlib.pyplot
# -----------------------------------------------------------------------------

# Numpy: Salaries generation
# Pandas: Days generation
def gen_dataset() -> dict[str, Any]:
    np.random.seed(42)  # Let's look always for the same numbers
    x = pd.date_range(start="2024-01-01", periods=1000)
    y = np.random.normal(loc=980, scale=200, size=1000)
    return {"Days": x, "Salaries": y}


# Pandas: Table generation with Days (x) and Salaries (y)
# Matplotlib.pyplot: Matrix generation and export
def gen_matrix(dataset: dict[str, Any]) -> None:
    pd.options.display.float_format = '{:.2f}'.format

    df = pd.DataFrame(dataset)  # DataFrame - table with Days and Salaries cols
    df = df[df['Salaries'] > 920]  # Reduce table to salaries > 920
    df_monthly = df.resample('ME', on='Days').mean()  # Month End - monthly avg
    df_monthly.index = df_monthly.index.strftime('%b %y')  # dates format chang

    plt.plot(df_monthly.index, df_monthly['Salaries'])  # Plot - creates chart
    plt.title('Average Salaries Job Offers')
    plt.xticks(rotation=60)  # rotate x dates
    plt.tight_layout()  # adjust chart to fit all
    plt.savefig('matrix_analysis.png')  # save chart to a png file
    plt.show()


# ============================== Program Test ================================

def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\n💠 Checking dependencies:")
    pkg_list = {
        "Pandas": "Data manipulation ready",
        "Numpy": "Numerical computation ready",
        "Matplotlib": "Visualization ready"
        # "Tensorflow": "test"
    }
    validate_pkg(pkg_list)
    print("\n💠 Analyzing Matrix data...")
    print("💠 Processing 1000 data points...")
    print("💠 Generating visualization...")
    gen_matrix(gen_dataset())
    print("\n💠 Analysis complete!")
    print("✅ Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
