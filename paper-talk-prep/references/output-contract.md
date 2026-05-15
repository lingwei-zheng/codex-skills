# Output Contract

Use this contract when producing slide-by-slide talk preparation artifacts.

## Default Structure

```text
Slide 1. <title>
Goal: <what this slide must accomplish>
On-slide text:
- <short line>
- <short line>
Visual suggestion: <figure / table / diagram / no visual>
Speaker notes:
<80-180 words of spoken explanation>
Transition: <one sentence leading into the next slide>
```

## Slide Archetypes

Use one of these rhetorical archetypes for each slide.

- `opening`: title, hook, talk promise
- `motivation`: why the problem matters
- `problem`: exact research gap or question
- `intuition`: simple explanation before details
- `method`: pipeline, architecture, procedure, or identification strategy
- `data`: dataset, study area, sample, or experimental setup
- `results`: main finding
- `ablation`: robustness, error analysis, or comparison
- `limitation`: boundaries and caveats
- `takeaway`: contribution, implication, or closing message

## Speaker Notes Rules

- Write for oral delivery, not for publication.
- Prefer short spoken sentences.
- Expand abbreviations the first time they appear unless the audience is clearly expert.
- Mention what the audience should notice in the visual.
- State why the slide matters before moving to the next one.

## On-Slide Text Rules

- Keep bullets parallel and compact.
- Avoid more than 4-5 bullets on a normal slide.
- Prefer labels such as `Problem`, `Method`, `Result`, `Why it matters` when they help scanning.
- Replace prose with equations, metrics, or keywords when the audience can parse them quickly.

## Optional Variants

### Outline Only

```text
Slide 1. <title> - <one-line purpose>
Slide 2. <title> - <one-line purpose>
```

### Full Script

After the slide-by-slide contract, add:

```text
Full script:
<continuous talk script aligned to the slide order>
```
