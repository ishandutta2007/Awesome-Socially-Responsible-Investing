import re
import os
import subprocess

repo_dir = r'C:\Users\ishan\Documents\Projects\Awesome-Socially-Responsible-Investing'
readme_path = os.path.join(repo_dir, 'README.md')

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, cwd=repo_dir, check=False)

def read_readme():
    with open(readme_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_readme(text):
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(text)

# Step 1: SaaS Size and Sort
text = read_readme()
old_saas = """| Platform | Description | Pricing |
|----------|-------------|---------|
| **[OpenInvest](https://openinvest.com)** | Personalized SRI portfolios with custom impact themes and values-based investing. | Varies by AUM (B2B focus). No free tier. |
| **[Ethic](https://ethic.com)** | Impact-focused investing platform allowing users to build portfolios aligned with specific values and ESG criteria. | Varies by AUM. No free tier. |
| **[Ellevest](https://ellevest.com)** | Women-focused robo-advisor with SRI options emphasizing gender equality and social impact. | $1 to $9 per month. No free tier. |
| **[Aspiration](https://aspiration.com)** | Sustainable banking and investing with fossil-free options and impact focus. | "Pay what is fair" ($0/mo minimum). Free tier limits: Basic features; Plus is $7.99/mo. |
| **[Betterment SRI Portfolios](https://betterment.com)** | Robo-advisor offering Broad Impact, Climate Impact, and Social Impact portfolios alongside traditional options. | 0.25% AUM (Digital), 0.40% AUM (Premium). No free tier. |"""
lines = [
    '| **[OpenInvest](https://openinvest.com)** | Personalized SRI portfolios with custom impact themes and values-based investing. | Varies by AUM (B2B focus). No free tier. | ~$100M Valuation |',
    '| **[Ethic](https://ethic.com)** | Impact-focused investing platform allowing users to build portfolios aligned with specific values and ESG criteria. | Varies by AUM. No free tier. | ~$150M Valuation |',
    '| **[Ellevest](https://ellevest.com)** | Women-focused robo-advisor with SRI options emphasizing gender equality and social impact. | $1 to $9 per month. No free tier. | ~$1.5B AUM |',
    '| **[Aspiration](https://aspiration.com)** | Sustainable banking and investing with fossil-free options and impact focus. | "Pay what is fair" ($0/mo minimum). Free tier limits: Basic features; Plus is $7.99/mo. | ~$1B Valuation |',
    '| **[Betterment SRI Portfolios](https://betterment.com)** | Robo-advisor offering Broad Impact, Climate Impact, and Social Impact portfolios alongside traditional options. | 0.25% AUM (Digital), 0.40% AUM (Premium). No free tier. | ~$1.3B Valuation |'
]
ordered = [lines[2], lines[4], lines[3], lines[1], lines[0]]
header = '| Platform | Description | Pricing | Company Size |\n|----------|-------------|---------|--------------|\n'
new_saas = header + '\n'.join(ordered)
if old_saas in text:
    text = text.replace(old_saas, new_saas)
write_readme(text)
run_cmd('git add . ;git commit -m "Added company size and sorted the SaaS based on that";git push;')

# Step 2: Open Source Stars and Sort
text = read_readme()
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
write_readme(text)
run_cmd('git add . ;git commit -m "Added github stars and sorted the opensource based on that";git push;')

# Step 3: Decorate the README banner (svg in assets/)
assets_dir = os.path.join(repo_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)
banner_path = os.path.join(assets_dir, 'banner.svg')
svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:rgb(34,193,195);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(253,187,45);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" rx="15" ry="15"/>
  <text x="50%" y="40%" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white" text-anchor="middle" alignment-baseline="middle">Awesome SRI &amp; ESG Investing</text>
  <text x="50%" y="65%" font-family="Arial, sans-serif" font-size="20" fill="white" text-anchor="middle" alignment-baseline="middle">Empowering Sustainable Portfolios</text>
  <circle cx="50" cy="50" r="20" fill="white" opacity="0.3">
    <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="750" cy="150" r="15" fill="white" opacity="0.3">
    <animate attributeName="r" values="15;25;15" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>'''
with open(banner_path, 'w', encoding='utf-8') as f:
    f.write(svg_content)

text = read_readme()
banner_md = '<div align="center">\n  <img src="assets/banner.svg" alt="Awesome SRI Banner" width="100%">\n</div>\n\n'
if not text.startswith('<div align="center">'):
    text = banner_md + text
write_readme(text)
run_cmd('git add .  && git commit -m "added banner" && git push')

# Step 4: Decorate README with emojis
text = read_readme()
text = text.replace('## Top Socially Responsible', '## 🌍 Top Socially Responsible')
text = text.replace('## SaaS / Cloud-Hosted', '## ☁️ SaaS / Cloud-Hosted')
text = text.replace('### Leading Options', '### 🚀 Leading Options')
text = text.replace('## Open-Source / Self-Hosted Alternatives', '## 💻 Open-Source / Self-Hosted Alternatives')
text = text.replace('### Featured Projects', '### 🌟 Featured Projects')
text = text.replace('### Additional Open-Source Tools', '### 🛠️ Additional Open-Source Tools')
text = text.replace('## Comparison', '## ⚖️ Comparison')
text = text.replace('## Getting Started', '## 🏁 Getting Started')
text = text.replace('## Contributing', '## 🤝 Contributing')
write_readme(text)
run_cmd('git add .  && git commit -m "added emojis" && git push')

# Step 5: SEO Optimised
text = read_readme()
seo_header = '''<meta name="description" content="A curated guide to leading SaaS/cloud-hosted SRI/ESG investing platforms and their open-source/self-hosted equivalents. Focuses on sustainable finance, environmental, social, and governance investments." />
<meta name="keywords" content="SRI, ESG, socially responsible investing, sustainable finance, open-source investing, robo-advisor, climate investing" />

'''
if '<meta name="description"' not in text:
    text = text.replace('# Awesome-Socially-Responsible-Investing\n', '# Awesome-Socially-Responsible-Investing\n\n' + seo_header)
write_readme(text)
run_cmd('git add .  && git commit -m "seo optimised" && git push')

# Step 6: Badges to left
text = read_readme()
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a> '
if left_badges not in text:
    text = text.replace('# Awesome-Socially-Responsible-Investing\n', '# Awesome-Socially-Responsible-Investing\n\n' + left_badges + '\n')
write_readme(text)
run_cmd('git add .  && git commit -m "badges to left added" && git push')

# Step 7: Badges to right
text = read_readme()
right_badge = ' <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
if right_badge not in text:
    # Append to the same line as left_badges if possible
    text = text.replace(left_badges + '\n', left_badges + right_badge + '\n')
write_readme(text)
run_cmd('git add .  && git commit -m "badges to right added" && git push')

# Step 8: Star History
text = read_readme()
star_history = '''
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Socially-Responsible-Investing&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Socially-Responsible-Investing&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Socially-Responsible-Investing&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Socially-Responsible-Investing&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''
if '## ⭐ Star History' not in text and '##  Star History' not in text:
    text += star_history
write_readme(text)
run_cmd('git add . ;git commit -m "star history added";git push;')

# Step 9: Replace chartrepos with chart?repos
text = read_readme()
text = text.replace('chartrepos', 'chart?repos')
write_readme(text)
run_cmd('git add . ;git commit -m "fixed star plot";git push;')

# Step 10: Replace valid awesome link
text = read_readme()
text = text.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
write_readme(text)
run_cmd('git add . ;git commit -m "invalid awesome link fixed";git push;')
