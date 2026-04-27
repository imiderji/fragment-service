# Fragment Service

```text
  ________________________________
 /                                \
|  text -> chunk -> store -> use   |
|__________________________________|
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Fragment Service is a lightweight service for working with text fragments and chunks.
It is designed to split text into manageable pieces, organize them, and make them easier to process in downstream pipelines such as search, retrieval, indexing, and LLM workflows.

In short, this service helps turn raw text into structured, reusable chunks.

Run service

```bash
uv run fragment-service
```
