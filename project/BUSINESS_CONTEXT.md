# Business context

## Decision and stakeholder
SOC analysts spend time joining alerts and event records into a defensible incident narrative. Alert severity alone does not explain chronology, related entities, uncertainty or the next investigation step.

Users: SOC analyst, incident investigator and shift handover lead. A domain reviewer owns factual approval; the delivery lead owns release acceptance. The assistant reduces evidence assembly time while preserving human accountability.

## Before and after
Before: a reviewer assembles a narrative manually and struggles to trace individual statements. After: the reviewer receives structured candidates with original evidence, corrects uncertainty, then approves an auditable export.

## Value measurement
Use at least five comparable tasks per reviewer. Record manual baseline minutes, assisted preparation minutes, review minutes, correction count and accepted output quality. Report median end-to-end time change and the sample size. Target ≥20% reduction without lowering factual accuracy; a small sample is exploratory, not a universal productivity claim.

## Risks and limits
Synthetic telemetry is not evidence of production detection performance. Host/user co-occurrence is not causation, and a security alert is not confirmed compromise. Clock offsets and missing events can invalidate apparent sequences.

Possible impact statements are explicitly provisional. Human judgement and source inspection remain part of the workflow.
