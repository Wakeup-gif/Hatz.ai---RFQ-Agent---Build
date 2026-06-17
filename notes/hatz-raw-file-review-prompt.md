# Hatz.ai Raw File Review Prompt

Use this prompt if Hatz.ai can see the GitHub repo structure but cannot reliably scrape rendered GitHub `blob` pages. Ask it to read the raw file URLs instead.

```text
The GitHub blob pages may not render cleanly in your scraper. Please use the raw GitHub URLs below instead of `/blob/main/` URLs.

Repository:
https://github.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build

Raw files to inspect first:

1. README
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/README.md

2. Hatz architecture
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/hatz-architecture.md

3. Hatz readiness gates
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/hatz-readiness-gates.md

4. Hatz response next steps
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/deployment/hatz-response-next-steps.md

5. Deployment operations decision matrix
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/deployment/operations-decision-matrix.md

6. Hatz workspace unknowns
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/notes/hatz-workspace-unknowns.md

7. Hatz discovery prompt
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/notes/hatz-ai-discovery-prompt.md

8. Repo pull prompt
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/notes/hatz-repo-pull-prompt.md

9. Core agent
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/agent.py

10. Hatz adapter
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/adapters/hatz_adapter.py

11. Runtime contract
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/contracts/runtime_contract.py

12. Readiness evaluator
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/validation/readiness.py

13. Deployment matrix code
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/validation/deployment.py

14. Runtime instructions source package
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/source-package/quick-rfq-summary-app-v1.5/02-runtime-instructions.md

15. Output contract source package
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/source-package/quick-rfq-summary-app-v1.5/03-output-contract.md

Please inspect these raw files and provide:

1. What can be implemented directly in Hatz.ai.
2. What should be translated from Python into native Hatz prompt/workflow logic.
3. What requires Hatz support confirmation.
4. Recommended workflow shape: input → source handling → summarizer → status branch → human review → evidence → pilot/go-no-go.
5. Any changes needed to make the repo easier for Hatz.ai to ingest.
```
