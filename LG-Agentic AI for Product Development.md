# Agentic AI for Product Development
**Course Code:** TGS-2024045799
**Version:** v7.0
**TSC:** ICT-TEM-4035-1.1 Automation Management in Product Development
## Learning outcomes
- LO1 Evaluate agentic AI builders for product research and development, comparing strengths, limitations, resources and skills.
- LO2 Apply optimisation techniques to improve the efficiency, quality and control of agentic product-development workflows.
- LO3 Evaluate the benefits and trade-offs of deploying agentic AI-powered product solutions and recommend a governed path forward.

## End-to-end architecture
1. Surface and applicability decision
2. Repository reconnaissance and scoped instruction hierarchy
3. Outcome contract, plan and permission boundary
4. Minimal implementation and reviewed diff
5. Focused tests, regression checks and browser evidence
6. Golden-task comparison against baseline
7. Human-governed pilot, expand, hold or stop decision

## Topic 1: Evaluating Agentic AI Tools for Product Research and Development

Identify a product opportunity, map it to a suitable agentic pattern, and compare builders using evidence, readiness and total-cost criteria.

### Agentic AI versus assistants

**Mechanism:** Receive goal → Plan work → Use tools → Adapt from results
**Fields:** goal, plan, tool_call, observation
**Measure:** Goal completion rate with valid evidence
**Control:** Require a multi-step loop, tool boundary and stop condition before calling a system agentic.
**Evidence:** Trace showing plan, tool result and final decision

### Product lifecycle application map

**Mechanism:** Discover need → Define concept → Deliver prototype → Learn in market
**Fields:** insight, hypothesis, artifact, feedback
**Measure:** % lifecycle stages with a named human owner
**Control:** Map each agent task to one lifecycle decision and accountable role.
**Evidence:** Lifecycle map with task-owner pairs

### Opportunity framing

**Mechanism:** Observe friction → Name user → Quantify impact → Frame outcome
**Fields:** problem, user, baseline, target
**Measure:** Validated problem statements / total ideas
**Control:** Start with observable friction and a measurable outcome, not a tool demonstration.
**Evidence:** Opportunity brief with baseline and target

### Jobs-to-be-done lens

**Mechanism:** Capture situation → Identify progress → Expose obstacle → Define success
**Fields:** situation, job, barrier, outcome
**Measure:** % research observations linked to a user job
**Control:** Write needs as progress users seek in a real context.
**Evidence:** JTBD statement linked to verbatim research notes

### Research-agent pattern

**Mechanism:** Set question → Gather sources → Triangulate claims → Synthesize insight
**Fields:** question, source, claim, confidence
**Measure:** % material claims supported by two independent sources
**Control:** Require source provenance, claim-level support and uncertainty labels.
**Evidence:** Research ledger and cited insight brief

### Competitor intelligence workflow

**Mechanism:** Choose peers → Freeze criteria → Collect evidence → Compare gaps
**Fields:** peer, criterion, evidence, gap
**Measure:** Comparable criteria populated per competitor
**Control:** Freeze the same criteria and observation date before collection.
**Evidence:** Timestamped comparison matrix

### Voice-of-customer synthesis

**Mechanism:** Ingest feedback → Cluster themes → Test outliers → Prioritise need
**Fields:** feedback_id, theme, outlier, priority
**Measure:** % themes traceable to source rows
**Control:** Retain row-level traceability and inspect negative cases separately.
**Evidence:** Theme table with supporting and contradicting excerpts

### Persona and assumption map

**Mechanism:** Group evidence → Draft persona → Label assumptions → Plan validation
**Fields:** segment, need, assumption, test
**Measure:** High-risk assumptions with a validation test
**Control:** Mark inferred attributes and separate evidence from hypothesis.
**Evidence:** Persona card plus assumption register

### Agentic builder landscape

**Mechanism:** Define use case → Shortlist builders → Run common task → Score fit
**Fields:** use_case, builder, test_case, score
**Measure:** Weighted score on a common golden task
**Control:** Run the same input, output and constraints across every candidate.
**Evidence:** Paired trial results and recommendation

### Workflow versus autonomous agent

**Mechanism:** Assess variability → Assess risk → Choose pattern → Set override
**Fields:** variability, risk, pattern, override
**Measure:** % high-risk steps on deterministic paths
**Control:** Use the simplest architecture that satisfies variability and judgment needs.
**Evidence:** Pattern decision with rejected alternatives

### Build-buy-partner decision

**Mechanism:** Clarify advantage → Estimate capability → Model ownership → Select posture
**Fields:** advantage, capability, ownership_cost, posture
**Measure:** Risk-adjusted value over total cost of ownership
**Control:** Include change, integration, assurance and exit costs.
**Evidence:** Three-option decision table with sensitivity range

### Resource and skills readiness

**Mechanism:** List capabilities → Assess gaps → Plan controls → Sequence pilot
**Fields:** data, people, platform, governance
**Measure:** Critical readiness gaps closed before pilot
**Control:** Gate pilot entry on minimum data, product, technical and risk capabilities.
**Evidence:** Readiness heatmap and action owners

### Evaluation decision matrix

**Mechanism:** Weight criteria → Score evidence → Test sensitivity → Recommend
**Fields:** weight, score, sensitivity, decision
**Measure:** Recommendation stability across plausible weights
**Control:** Agree criteria before testing and show how weight changes affect the result.
**Evidence:** Weighted matrix, caveats and decision owner

## Topic 2: Building and Optimising Agentic Product Development Workflows

Translate product intent into bounded agent roles, specifications, hand-offs, evaluation sets and an iterative prototype workflow that improves with evidence.

### Goal-plan-act-observe loop

**Mechanism:** Interpret goal → Choose next step → Act through tool → Observe state
**Fields:** goal, next_action, tool_result, status
**Measure:** % loops ending in a verified stop state
**Control:** Use explicit budgets, stop conditions and observable state transitions.
**Evidence:** Loop trace with terminal status

### Product context packet

**Mechanism:** State vision → Name users → Add constraints → Define evidence
**Fields:** vision, users, constraints, acceptance
**Measure:** Required context fields present before execution
**Control:** Version a compact context packet and expose unknowns explicitly.
**Evidence:** Context file and assumption log

### Outcome-focused specification

**Mechanism:** Describe problem → Define behavior → Set boundaries → Specify done
**Fields:** problem, behavior, non_goals, acceptance
**Measure:** % acceptance criteria observable by reviewer
**Control:** Describe what must be true and what must not change.
**Evidence:** PRD section with testable criteria

### User stories and acceptance criteria

**Mechanism:** Name actor → State intent → Explain value → Write examples
**Fields:** actor, intent, value, examples
**Measure:** % stories with positive, edge and failure examples
**Control:** Attach concrete examples and negative conditions to each story.
**Evidence:** Story map with example-based acceptance

### Journey-map orchestration

**Mechanism:** Map stages → Locate friction → Assign agent role → Keep human gate
**Fields:** stage, friction, agent_role, gate
**Measure:** % high-consequence moments with human control
**Control:** Preserve recovery, explanation and control at consequential journey points.
**Evidence:** Journey map with agent and human swimlanes

### Single-agent baseline

**Mechanism:** Bound one goal → Connect minimal tools → Run baseline → Measure gaps
**Fields:** goal, tools, baseline, gaps
**Measure:** Accepted tasks per 20-case evaluation set
**Control:** Prove the minimum viable agent before adding roles.
**Evidence:** Baseline run log and failure summary

### Multi-agent role design

**Mechanism:** Decompose domains → Assign role → Limit authority → Define coordinator
**Fields:** domain, role, authority, coordinator
**Measure:** Handoffs that add unique value / total handoffs
**Control:** Give each role distinct inputs, output schema and decision rights.
**Evidence:** Role charter and responsibility matrix

### Handoff contract

**Mechanism:** Validate input → Perform task → Emit schema → Acknowledge receipt
**Fields:** input_schema, task, output_schema, ack
**Measure:** % handoffs passing schema validation
**Control:** Use stable identifiers, structured outputs and fail-closed validation.
**Evidence:** Handoff record with validation status

### Tool and retrieval grounding

**Mechanism:** Identify need → Select source → Retrieve context → Cite evidence
**Fields:** need, source, context, citation
**Measure:** % answer claims grounded in approved sources
**Control:** Constrain sources, retain citations and test retrieval misses.
**Evidence:** Retrieved evidence linked to output claims

### Prompt contract design

**Mechanism:** State objective → Provide context → Set constraints → Define format
**Fields:** objective, context, constraints, output_schema
**Measure:** First-pass outputs meeting all contract fields
**Control:** Separate goal, context, rules, examples and output contract.
**Evidence:** Prompt version and conformance checklist

### Evaluation-set engineering

**Mechanism:** Sample real tasks → Add edge cases → Freeze expected traits → Score runs
**Fields:** task_id, input, expected, score
**Measure:** Coverage across core, edge and adversarial cases
**Control:** Build a representative frozen set before optimisation.
**Evidence:** Versioned evaluation CSV and score report

### Iteration and error taxonomy

**Mechanism:** Classify failure → Find causal layer → Apply one change → Re-run set
**Fields:** failure_type, layer, change, delta
**Measure:** Improvement on failed cases without regression
**Control:** Change one causal layer per experiment and re-run the full frozen set.
**Evidence:** Experiment ledger with before-after deltas

### Prototype-to-learning loop

**Mechanism:** Build thin slice → Expose to users → Capture signal → Revise hypothesis
**Fields:** prototype, test, signal, hypothesis
**Measure:** Validated assumptions per prototype cycle
**Control:** Time-box builds and define the decision each prototype must unlock.
**Evidence:** Experiment brief and go-pivot-stop decision

## Topic 3: Deploying and Evaluating Agentic AI-Powered Product Solutions

Design a deployment posture that preserves human control, security, observability, cost discipline and a production feedback loop.

### Prototype-to-production gate

**Mechanism:** Validate value → Validate behavior → Assess operations → Approve handoff
**Fields:** value, evals, operability, decision
**Measure:** Required gates passed before production investment
**Control:** Separate learning code from supported production architecture and evidence.
**Evidence:** Handoff pack with eval set, edge cases and prompt strategy

### Deployment channel fit

**Mechanism:** Map user context → Assess channel limits → Design fallback → Select channel
**Fields:** context, channel, fallback, choice
**Measure:** Task completion and recovery rate by channel
**Control:** Compare web, workspace, messaging and embedded channels on task and risk.
**Evidence:** Channel matrix and fallback path

### Reference deployment architecture

**Mechanism:** Receive request → Orchestrate agent → Access tools → Record outcome
**Fields:** request_id, orchestrator, tool_policy, audit_event
**Measure:** % transactions traceable end to end
**Control:** Carry a stable request identifier through every component.
**Evidence:** Architecture diagram and correlated trace

### API and integration contract

**Mechanism:** Authenticate caller → Validate request → Execute bounded action → Return status
**Fields:** identity, schema, action, status
**Measure:** % requests with schema-valid input and explicit outcome
**Control:** Use typed schemas, idempotency and explicit error states.
**Evidence:** API contract and negative-test results

### Programming skill mix

**Mechanism:** Specify behavior → Read interfaces → Test integration → Operate service
**Fields:** prompting, api, testing, operations
**Measure:** Critical skill roles assigned with accountable owners
**Control:** Plan the product, prompt, data, integration, testing and operations skills explicitly.
**Evidence:** Skills matrix and gap plan

### Security and privacy boundary

**Mechanism:** Classify data → Minimise access → Protect tools → Audit use
**Fields:** data_class, permission, tool_policy, audit
**Measure:** % sensitive paths protected by least privilege
**Control:** Layer input controls, tool allowlists, approval and monitoring.
**Evidence:** Threat model, permission map and tested controls

### Human oversight design

**Mechanism:** Classify consequence → Set confidence gate → Route exception → Record decision
**Fields:** risk_class, threshold, reviewer, decision
**Measure:** % consequential actions with meaningful human review
**Control:** Show the evidence and consequence at the point of decision.
**Evidence:** Approval log tied to current output

### Observability and product KPIs

**Mechanism:** Instrument event → Compute metric → Segment failure → Trigger action
**Fields:** event, metric, segment, action
**Measure:** North-star outcome plus quality, cost and risk guardrails
**Control:** Pair business outcomes with reliability, safety and experience measures.
**Evidence:** Metric tree and alert ownership

### Quality, latency and cost frontier

**Mechanism:** Measure quality → Measure latency → Load full cost → Choose frontier
**Fields:** quality, latency, cost, posture
**Measure:** Accepted outcome cost at target response time
**Control:** Compare only configurations meeting minimum quality and risk thresholds.
**Evidence:** Pareto chart and selected operating point

### Production evaluation loop

**Mechanism:** Sample traffic → Score outcomes → Review failures → Release repair
**Fields:** sample, score, failure, release
**Measure:** % production samples scored and actioned
**Control:** Combine frozen regression sets with representative live sampling.
**Evidence:** Eval dashboard and linked repair record

### Rollout and change management

**Mechanism:** Pilot cohort → Train users → Expand gradually → Retire safely
**Fields:** cohort, enablement, gate, rollback
**Measure:** Cohorts expanded only after approved thresholds
**Control:** Use staged rollout, telemetry, support playbooks and rollback criteria.
**Evidence:** Rollout plan with go/no-go gates

### Feedback and graceful failure

**Mechanism:** Detect uncertainty → Explain limit → Offer recovery → Learn from feedback
**Fields:** uncertainty, message, recovery, feedback
**Measure:** Successful recovery rate after agent failure
**Control:** Design honest limits, user control and a path to human help.
**Evidence:** Failure-state prototype and feedback taxonomy

### Benefit-trade-off recommendation

**Mechanism:** Quantify benefit → Price risk → Test scenarios → Recommend posture
**Fields:** benefit, risk, scenario, recommendation
**Measure:** Net value remains positive under downside scenarios
**Control:** Use risk-adjusted scenarios and issue a pilot, expand, hold or stop decision.
**Evidence:** Executive decision memo with conditions and owner

## Activities

### Activity 01: Frame a Product Opportunity

Turn synthetic stakeholder notes into a measurable agentic-AI opportunity brief.

- Folder: `activities/activity-01-opportunity-brief/`
- Workflow: Inspect notes, Name user, Quantify friction, Define outcome, List assumptions, Set validation
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Every claim traces to a source row; the outcome is measurable; high-risk assumptions have named tests.

### Activity 02: Compare Agentic AI Builders

Run a common product-research task across three synthetic builder profiles and select a fit-for-purpose option.

- Folder: `activities/activity-02-builder-comparison/`
- Workflow: Freeze task, Set criteria, Score builders, Apply weights, Test sensitivity, Recommend
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Scores use one common task, weights total 100%, and the recommendation survives or explains sensitivity.

### Activity 03: Build a Research Evidence Pack

Transform mock market and competitor records into a traceable, uncertainty-aware insight brief.

- Folder: `activities/activity-03-research-evidence-pack/`
- Workflow: Load records, Normalise facts, Triangulate claims, Flag conflict, Rank insight, Cite sources
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Material insights cite at least two records or explicitly state single-source uncertainty.

### Activity 04: Create Persona and JTBD Map

Derive evidence-based personas and jobs-to-be-done without presenting generated assumptions as facts.

- Folder: `activities/activity-04-persona-jtbd-map/`
- Workflow: Cluster needs, Draft persona, Write JTBD, Label inference, Rank risk, Plan test
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Persona needs trace to source IDs; assumptions are labelled; each risky assumption has a feasible validation test.

### Activity 05: Design an Agent Workflow Canvas

Map a product-discovery task into an agentic loop with tools, state, stop conditions and human gates.

- Folder: `activities/activity-05-agent-workflow-canvas/`
- Workflow: Define goal, Map stages, Assign tools, Set schemas, Add gates, Set stop
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Every stage has an owner and observable output; consequential actions stop for human review.

### Activity 06: Create an AI-Ready PRD

Convert an opportunity brief into outcome-focused requirements, user stories and acceptance examples.

- Folder: `activities/activity-06-prd-and-user-stories/`
- Workflow: Restate problem, Define behavior, Write stories, Add examples, Set non-goals, Review gaps
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Requirements are testable, non-goals are explicit, and every priority story has three acceptance examples.

### Activity 07: Engineer a Prompt and Evaluation Set

Create a structured prompt contract and a frozen evaluation set for a product-feedback agent.

- Folder: `activities/activity-07-prompt-evaluation-set/`
- Workflow: Define contract, Sample cases, Add edges, Freeze rubric, Run baseline, Record gaps
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: The evaluation set covers all segments; scoring rules are reproducible; baseline failures are retained.

### Activity 08: Run a Prototype Experiment

Evaluate a synthetic agent prototype, classify failures and recommend one causal improvement.

- Folder: `activities/activity-08-prototype-experiment/`
- Workflow: Run baseline, Score outputs, Classify failure, Change one layer, Re-run set, Decide
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: The change targets one causal layer, the frozen set is preserved, and regression risk is documented.

### Activity 09: Select a Deployment Posture

Compare channel and architecture options for an agentic product using task, integration and risk evidence.

- Folder: `activities/activity-09-deployment-decision/`
- Workflow: Map context, Compare channels, Select architecture, Add fallback, Cost posture, Approve
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: The selected option meets task, integration, safety and recovery thresholds; caveats are explicit.

### Activity 10: Conduct a Risk and Control Review

Threat-model an agent workflow and assign layered controls, evidence and owners.

- Folder: `activities/activity-10-risk-control-review/`
- Workflow: Map assets, Identify threats, Score exposure, Select controls, Assign owner, Test control
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: High risks have preventive and detective controls, named owners and testable evidence.

### Activity 11: Design KPI and Feedback Dashboard

Create a metric tree and monitoring view that balances business value, quality, experience, cost and risk.

- Folder: `activities/activity-11-kpi-feedback-dashboard/`
- Workflow: Set outcome, Add guardrails, Define events, Set thresholds, Assign action, Review drift
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Metrics have formulas, data sources, thresholds, segments and action owners; no vanity-only measure drives release.

### Activity 12: Deliver a Governed Product Recommendation

Synthesize value, evaluation, readiness and risk evidence into an executive pilot, expand, hold or stop decision.

- Folder: `activities/activity-12-executive-recommendation/`
- Workflow: Summarise value, Compare evidence, Price risk, Test downside, Set conditions, Recommend
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: The recommendation is traceable to evidence, survives a downside scenario, and has measurable exit criteria.

## References
- [Current course page](https://www.tertiarycourses.com.sg/wsq-agentic-ai-for-product-development.html) — Course identity, duration, learning outcomes, topics and assessment format
- AI Product Management: Local reference/AI Product Management.pdf — AI-PM playground, natural-language development, rapid prototyping, specification, iteration and production handoff
- Building AI-Powered Products: Local reference/Building AI-Powered Products.pdf — AI product-development lifecycle, product sense, goals and metrics, agent patterns, evaluation and production rollout
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Agent/workflow distinction, simple composable patterns and complexity trade-offs
- [People + AI Guidebook](https://pair.withgoogle.com/guidebook-v2/) — User needs, success definition, mental models, feedback, control and graceful failure
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — Govern, map, measure and manage risk throughout the AI lifecycle
