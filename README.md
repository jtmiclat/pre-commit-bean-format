# pre-commit-bean-format

Format `.beancount` files using [bean-format](https://beancount.github.io/docs/running_beancount_and_generating_reports.html#bean-format)

## Usage

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/jtmiclat/pre-commit-bean-format
  rev: master # replace with commit sha
  hooks:
    - id: bean-format
```

This will run `bean-format` to all `.bean` and `.beancount` files

If you plan to use a different extension, you can pass a custom `files` using the files field.

For example, we have files with extension `.count`:

```yaml
- repo: https://github.com/jtmiclat/pre-commit-bean-format
  rev: master # replace with commit sha
  hooks:
    - id: bean-format
      files: \.count$
```

If you want to pin a certain version of `beancount` or other dependencies, you can add `additional_dependencies` field

For example, we want to pin `beancount` to certain version:

```yaml
- repo: https://github.com/jtmiclat/pre-commit-bean-format
  rev: master # replace with commit sha
  hooks:
    - id: bean-format
      additional_dependencies: ["beancount==2.3.6"]
```

If you want to pass additional arguments to format, you can add `args` field

For example:

```yaml
- repo: https://github.com/jtmiclat/pre-commit-bean-format
  rev: master # replace with commit sha
  hooks:
    - id: bean-format
      args: ["-w 100"]
```

# Credits

Forked from: https://github.com/whtsky/pre-commit-beancount-format/
