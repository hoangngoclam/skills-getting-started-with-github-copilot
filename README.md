# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey hoangngoclam!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/hoangngoclam/skills-getting-started-with-github-copilot/issues/1)

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)


---

**Run tests**

- **Install dependencies (venv recommended):**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- **Run tests (recommended - uses the venv python):**

```bash
# from the repository root
.venv/bin/python -m pytest -q
```

- **Alternative (without activating venv):**

```bash
# ensure src is on PYTHONPATH so tests can import the app
PYTHONPATH=src pytest -q
```

> Note: `requirements.txt` includes test dependencies (`httpx`, `pytest`) required by `starlette.testclient`/`fastapi.testclient`.

```