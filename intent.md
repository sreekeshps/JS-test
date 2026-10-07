# E2E Testing Agent — Hello World

A minimal "hello world" end-to-end testing AI agent built on the A2A protocol in Python, running on SAP BTP.

## Business challenge

Demonstrate a working, deployable E2E testing agent as a baseline for automated software quality assurance.

## Business Goals & Success Criteria

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Demonstrate a working E2E testing agent | — | Hello World agent running end-to-end | — | Software Quality Testing | user |

## Key Milestones

1. **Agent initialised** — Python A2A agent starts and responds to a health-check request.
2. **Hello World task executed** — Agent receives a test task and returns a structured result.
3. **E2E flow verified** — Full request-response cycle confirmed (client → agent → response).
4. **Tests pass** — Pre-built unit and server tests run green.

## Business Architecture (RBA)

### End-to-End Process

Idea to Release for Software

### Process Hierarchy

```
Idea to Release for Software (E2E)
└── Design to Release (software product)
    └── Design software product (BPS-320_005)
        └── Build software product
        └── Perform continuous testing
```

### Summary

The E2E testing agent maps to the "Design to Release" phase of the Idea to Release for Software process, specifically covering continuous testing and quality assurance activities for software products.

## Fit Gap Analysis

| Requirement (business) | Standard asset(s) found | API ORD ID | MCP Server ORD ID | MCP Server Version | Gap? | Notes / assumptions |
|------------------------|------------------------|------------|-------------------|--------------------|------|---------------------|
| Automated E2E test execution | No standard SAP product covers this directly | — | — | — | Yes | Custom Python A2A agent required |
| Test result reporting | SAP Cloud ALM Test Automation (REST) | — | — | — | Maybe | Available API but no MCP server found |

### Key findings

- No standard SAP product directly provides an autonomous E2E testing agent — custom development is required.
- SAP Cloud ALM offers Test Automation and Test Management APIs that can be integrated in future iterations.
- The A2A protocol (Python) is the right foundation for this agent type.
- Hello World scope keeps the milestone simple: a working agent loop with a test task and structured response.
- Future extensions can hook into SAP Cloud ALM APIs for full test lifecycle management.

## Recommendations

### Hello World E2E Testing Agent

#### Executive Summary

Minimal Python A2A agent demonstrating a working E2E test loop on SAP BTP.

#### Recommended Solution

A pro-code Python agent using the A2A protocol, deployed on SAP BTP. The agent accepts a test task, executes a hello-world test scenario, and returns a structured result. Built with OpenTelemetry instrumentation and pre-built tests included.

#### Recommended solution category

AI Agent

#### Intent fit
95%
