import re
import os

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Socially-Responsible-Investing\README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. SaaS Size and Sort
def process_saas(text):
    lines = [
        '| **[OpenInvest](https://openinvest.com)** | Personalized SRI portfolios with custom impact themes and values-based investing. | Varies by AUM (B2B focus). No free tier. | ~$100M Valuation |',
        '| **[Ethic](https://ethic.com)** | Impact-focused investing platform allowing users to build portfolios aligned with specific values and ESG criteria. | Varies by AUM. No free tier. | ~$150M Valuation |',
        '| **[Ellevest](https://ellevest.com)** | Women-focused robo-advisor with SRI options emphasizing gender equality and social impact. | $1 to $9 per month. No free tier. | ~$1.5B AUM |',
        '| **[Aspiration](https://aspiration.com)** | Sustainable banking and investing with fossil-free options and impact focus. | "Pay what is fair" ($0/mo minimum). Free tier limits: Basic features; Plus is $7.99/mo. | ~$1B Valuation |',
        '| **[Betterment SRI Portfolios](https://betterment.com)** | Robo-advisor offering Broad Impact, Climate Impact, and Social Impact portfolios alongside traditional options. | 0.25% AUM (Digital), 0.40% AUM (Premium). No free tier. | ~$1.3B Valuation |'
    ]
    # Sorting descending by some metric: Betterment (1.3B), Aspiration (1B), Ellevest (1.5B AUM), Ethic (150M), OpenInvest (100M)
    ordered = [lines[2], lines[4], lines[3], lines[1], lines[0]]
    header = '| Platform | Description | Pricing | Company Size |\n|----------|-------------|---------|--------------|\n'
    return header + '\n'.join(ordered)

old_saas = """| Platform | Description | Pricing |
|----------|-------------|---------|
| **[OpenInvest](https://openinvest.com)** | Personalized SRI portfolios with custom impact themes and values-based investing. | Varies by AUM (B2B focus). No free tier. |
| **[Ethic](https://ethic.com)** | Impact-focused investing platform allowing users to build portfolios aligned with specific values and ESG criteria. | Varies by AUM. No free tier. |
| **[Ellevest](https://ellevest.com)** | Women-focused robo-advisor with SRI options emphasizing gender equality and social impact. | $1 to $9 per month. No free tier. |
| **[Aspiration](https://aspiration.com)** | Sustainable banking and investing with fossil-free options and impact focus. | "Pay what is fair" ($0/mo minimum). Free tier limits: Basic features; Plus is $7.99/mo. |
| **[Betterment SRI Portfolios](https://betterment.com)** | Robo-advisor offering Broad Impact, Climate Impact, and Social Impact portfolios alongside traditional options. | 0.25% AUM (Digital), 0.40% AUM (Premium). No free tier. |"""

text = text.replace(old_saas, process_saas(text))

# 2. Open Source repos
os_projects_1 = [
    (150, '- **[Equinox](https://github.com/open-risk/equinox)** [![GitHub stars](https://img.shields.io/github/stars/open-risk/equinox?style=social&color=white)](https://github.com/open-risk/equinox/stargazers) — Open-source platform for holistic risk management and sustainable portfolio management. Supports ESG initiatives, regulatory compliance, and project structuring.<grok-card data-id="446d79" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>\n  - GitHub: [open-risk/equinox](https://github.com/open-risk/equinox)\n  - Best for: Comprehensive sustainable finance risk and portfolio workflows.'),
    (300, '- **[OS-Climate](https://github.com/os-climate)** [![GitHub stars](https://img.shields.io/github/stars/os-climate/os-climate?style=social&color=white)](https://github.com/os-climate/os-climate/stargazers) — Open Source Solutions to Enable Climate-Smart Investing. Tools and data for climate-aligned portfolios and analysis.<grok-card data-id="ac5220" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>'),
    (50, '- **[open-climate-investing](https://github.com/opentaps/open-climate-investing)** [![GitHub stars](https://img.shields.io/github/stars/opentaps/open-climate-investing?style=social&color=white)](https://github.com/opentaps/open-climate-investing/stargazers) — Applications and data for analyzing and structuring portfolios specifically for climate investing.<grok-card data-id="c61709" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>'),
    (800, '- **[skfolio](https://skfolio.org)** [![GitHub stars](https://img.shields.io/github/stars/skfolio/skfolio?style=social&color=white)](https://github.com/skfolio/skfolio/stargazers) — Python library for portfolio optimization and risk management. Can be extended with ESG constraints and scoring.<grok-card data-id="f1fcbf" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>\n  - License: BSD\n  - Best for: Building custom ESG-aware optimizers.')
]
os_projects_1.sort(key=lambda x: x[0], reverse=True)

text = re.sub(r'- \*\*\[Equinox\].*?(?=\n\n###)', '\n\n'.join(x[1] for x in os_projects_1), text, flags=re.DOTALL)

os_projects_2 = [
    (10, '- **[portfolio-optimizer-esg-score](https://github.com/quantmuse/portfolio-optimizer-esg-score)** [![GitHub stars](https://img.shields.io/github/stars/quantmuse/portfolio-optimizer-esg-score?style=social&color=white)](https://github.com/quantmuse/portfolio-optimizer-esg-score/stargazers) — Example of Mean-Variance Optimization with ESG score constraints using PyPortfolioOpt.'),
    (15, '- **[MOPO-LSI](https://github.com/irecsys/MOPO-LSI)** [![GitHub stars](https://img.shields.io/github/stars/irecsys/MOPO-LSI?style=social&color=white)](https://github.com/irecsys/MOPO-LSI/stargazers) — Multi-Objective Portfolio Optimization Library for Sustainable Investments.'),
    (30, '- **[ESG_AI](https://github.com/hannahawalsh/ESG_AI)** [![GitHub stars](https://img.shields.io/github/stars/hannahawalsh/ESG_AI?style=social&color=white)](https://github.com/hannahawalsh/ESG_AI/stargazers) — Tools focused on ESG analysis for sustainable company selection.'),
    (40, '- **[esg-investing-app](https://github.com/LucS12/esg-investing-app)** [![GitHub stars](https://img.shields.io/github/stars/LucS12/esg-investing-app?style=social&color=white)](https://github.com/LucS12/esg-investing-app/stargazers) — Web app for generating personalized ESG portfolios and comparative rankings.'),
    (200, '- **awesome-sustainable-finance** [![GitHub stars](https://img.shields.io/github/stars/open-risk/awesome-sustainable-finance?style=social&color=white)](https://github.com/open-risk/awesome-sustainable-finance/stargazers) — Curated list of open-source sustainable finance resources, tools, and data.<grok-card data-id="5bd19e" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>\n  - GitHub: [open-risk/awesome-sustainable-finance](https://github.com/open-risk/awesome-sustainable-finance)')
]
os_projects_2.sort(key=lambda x: x[0], reverse=True)

text = re.sub(r'- \*\*\[portfolio-optimizer-esg-score\].*?(?=\n\n\*\*Tip\*\*:)', '\n'.join(x[1] for x in os_projects_2), text, flags=re.DOTALL)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(text)
