# ASF Levies Model – Windows Installation Guide (Regen Internal)

This guide walks you through setting up the `asf_levies_model` repository on a Windows machine using `venv` and `pip`, without needing Conda.

---

## 🔧 Prerequisites

Make sure you have:

- Python 3.10+
  - Install via Miniconda, python.org, or Windows Store
- Git
- [Optional] PyCharm for IDE support

---

## 📥 Step 1: Clone the Repository

Open PowerShell or your terminal and run:

    git clone https://github.com/nestauk/asf_levies_model.git
    cd asf_levies_model

---

## 🐍 Step 2: Create and Activate a Virtual Environment

Create the environment:

    python -m venv venv

Activate it:

    .\venv\Scripts\Activate.ps1

If you get a permission error, run this once:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

---

## 📦 Step 3: Install Dependencies

Install `requirements_dev.txt' file:
    
    pip install -r requirements_dev.txt

Install using the cleaned-up (Regen specific) `requirements.txt` file:

    pip install -r requirements.txt

If pip reports missing packages, you can install them individually (e.g., `pip install pandas`) and rerun the install.

---

## ⚙️ Step 4: Configure Data Paths (Optional)

If you're using local input files, update the file paths in `asf_levies_model/config/base.yaml`. For example:

    data_sources:
      ofgem_annex_4: "C:\\Users\\yourname\\Documents\\annex_4.xlsx"

Make sure to use double backslashes or forward slashes in Windows paths.

---

## 🧪 Step 5: Test the Installation

Create a file like `test_levy.py` and run this example:

    from asf_levies_model.levies import Levy

    levy = Levy(
        name="demo",
        short_name="d",
        electricity_weight=1,
        gas_weight=0,
        tax_weight=0,
        electricity_variable_weight=1,
        electricity_variable_rate=0.1,
        revenue=100,
        electricity_fixed_weight=0,
        electricity_fixed_rate=0,
        gas_variable_weight=0,
        gas_variable_rate=0,
        gas_fixed_weight=0,
        gas_fixed_rate=0,
        general_taxation=0
    )

    print(levy.calculate_levy(electricity_consumption=3.0, gas_consumption=0.0))

Expected output:

    0.30000000000000004

---

## 🧼 Notes

- Conda is not required; the original `environment.yaml` was Linux-specific and incompatible with Windows.
- This setup uses only necessary runtime dependencies (no dev tools or doc generators).
- If you want to lint or document, install optional dev tools separately (e.g., `black`, `flake8`, `sphinx`).

---

## 🆘 Troubleshooting

If you encounter issues:

- Ensure your virtual environment is activated (`(venv)` appears in terminal)
- Run `pip install --upgrade pip` to ensure your installer is up to date

## 🚀 How to Push Changes to GitHub

1. Check your Git status:

    `git status`

2. Add any updated/new files (e.g. requirements.txt, regen_install_guide.md):

    `git add requirements.txt regen_install_guide.md`

3. Commit the changes with a message:

    `git commit -m "Cleaned requirements.txt and added Windows install guide"`

4. Push to the remote repository:

    `git push origin main`

> If you're working on a branch other than `main`, replace `main` with your branch name:
>
>     git push origin your-branch-name

---

---
