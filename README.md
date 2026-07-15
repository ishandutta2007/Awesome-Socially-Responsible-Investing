# Awesome-Socially-Responsible-Investing
## Top Socially Responsible Investing (SRI/ESG) Platforms & Open-Source Alternatives

A curated guide to leading **SaaS/cloud-hosted SRI/ESG investing platforms** (like OpenInvest, Ethic, Ellevest, Aspiration, Betterment SRI) and their **open-source/self-hosted equivalents**. 

**Open-source solutions are emphasized** for transparency, customization, cost savings, and independence in sustainable finance.

---

## SaaS / Cloud-Hosted SRI/ESG Platforms

Popular platforms focused on aligning investments with environmental, social, and governance (ESG) values, impact, and ethical screening.

### Leading Options
- **[OpenInvest](https://openinvest.com)** — Personalized SRI portfolios with custom impact themes and values-based investing.
- **[Ethic](https://ethic.com)** — Impact-focused investing platform allowing users to build portfolios aligned with specific values and ESG criteria.
- **[Ellevest](https://ellevest.com)** — Women-focused robo-advisor with SRI options emphasizing gender equality and social impact.
- **[Aspiration](https://aspiration.com)** — Sustainable banking and investing with fossil-free options and impact focus.
- **[Betterment SRI Portfolios](https://betterment.com)** — Robo-advisor offering Broad Impact, Climate Impact, and Social Impact portfolios alongside traditional options.<grok-card data-id="95fdd6" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

**Other notables**: Wealthfront (SRI portfolio), EarthFolio (fully ESG/fossil-free), Vanguard ESG funds, and various robo-advisors with ESG overlays.

These platforms typically offer automated portfolio management, low fees (0.25%-1% AUM), and tools for values alignment.

---

## Open-Source / Self-Hosted Alternatives

These tools empower users and developers to build custom SRI/ESG strategies, portfolio optimizers, and analysis platforms without relying on commercial robo-advisors. Ideal for transparency in scoring, risk management, and sustainable finance.

### Featured Projects

- **[Equinox](https://github.com/open-risk/equinox)** — Open-source platform for holistic risk management and sustainable portfolio management. Supports ESG initiatives, regulatory compliance, and project structuring.<grok-card data-id="446d79" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>
  - GitHub: [open-risk/equinox](https://github.com/open-risk/equinox)
  - Best for: Comprehensive sustainable finance risk and portfolio workflows.

- **[OS-Climate](https://github.com/os-climate)** — Open Source Solutions to Enable Climate-Smart Investing. Tools and data for climate-aligned portfolios and analysis.<grok-card data-id="ac5220" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[open-climate-investing](https://github.com/opentaps/open-climate-investing)** — Applications and data for analyzing and structuring portfolios specifically for climate investing.<grok-card data-id="c61709" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>

- **[skfolio](https://skfolio.org)** — Python library for portfolio optimization and risk management. Can be extended with ESG constraints and scoring.<grok-card data-id="f1fcbf" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>
  - License: BSD
  - Best for: Building custom ESG-aware optimizers.

### Additional Open-Source Tools
- **[portfolio-optimizer-esg-score](https://github.com/quantmuse/portfolio-optimizer-esg-score)** — Example of Mean-Variance Optimization with ESG score constraints using PyPortfolioOpt.
- **[MOPO-LSI](https://github.com/irecsys/MOPO-LSI)** — Multi-Objective Portfolio Optimization Library for Sustainable Investments.
- **[ESG_AI](https://github.com/hannahawalsh/ESG_AI)** — Tools focused on ESG analysis for sustainable company selection.
- **[esg-investing-app](https://github.com/LucS12/esg-investing-app)** — Web app for generating personalized ESG portfolios and comparative rankings.
- **awesome-sustainable-finance** — Curated list of open-source sustainable finance resources, tools, and data.<grok-card data-id="5bd19e" data-type="citation_card" data-plain-type="render_inline_citation" ></grok-card>
  - GitHub: [open-risk/awesome-sustainable-finance](https://github.com/open-risk/awesome-sustainable-finance)

**Tip**: Combine Python libraries like **skfolio** or PyPortfolioOpt with ESG data sources (e.g., public datasets or APIs) to create self-hosted robo-advisor-like systems. Use Equinox/OS-Climate for production-grade climate and risk management.

---

## Comparison

| Aspect              | SaaS Platforms                        | Open-Source / Self-Hosted                  |
|---------------------|---------------------------------------|--------------------------------------------|
| **Cost**            | Management fees (0.25%-1% AUM)        | Free (only infra / data costs)             |
| **Customization**   | Limited to platform themes            | Full control over scoring, optimization, and data |
| **Transparency**    | Platform-defined ESG ratings          | Auditable code and methodologies           |
| **Setup Effort**    | Quick signup & automated              | Requires development / self-hosting        |
| **Use Case**        | Hands-off retail investors            | Developers, institutions, advanced users   |

---

## Getting Started

1. Identify your focus (climate impact, social equity, full ESG screening, etc.).
2. Explore **Equinox** and **OS-Climate** for robust sustainable finance infrastructure.
3. Use **skfolio** or similar libraries to build custom portfolio optimizers with ESG constraints.
4. Deploy via Docker, Python environments, or Jupyter for analysis.
5. Source ESG data from public APIs, government datasets, or open repositories.

## Contributing

Feel free to submit PRs to expand this list with more projects, tools, or comparisons!

**Last updated**: July 2026  
*Sustainable finance tools and data evolve quickly — always check the latest on GitHub repos and verify data sources.*