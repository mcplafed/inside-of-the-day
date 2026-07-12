# Publication operations

This repository is the canonical source for captions, visual assets, editable visual source, and series planning.

LinkedIn publisher scripts run outside this repository because they use local credentials and maintain idempotency state under `/root/outputs/`. Each publisher points to the frozen `caption.txt` and final `assets/infographic.png` in this repository.

Before scheduling or publishing:

1. Inspect the exact caption and final media in the post directory.
2. Run the appropriate publisher script with `--dry-run`.
3. Verify the visual remains 3240x4050 and the dry run reports `DRY_RUN_OK`.
4. Treat publication as proven only after HTTP 201 plus a LinkedIn post URL.
