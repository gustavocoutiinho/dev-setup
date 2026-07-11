# Salesforce CLI Development Deployment Skill

A focused skill for Claude Code to handle Salesforce development deployments correctly during iterative development workflows.

## What This Skill Does

This skill guides Claude to perform **development deployments** using the modern `sf` CLI. It focuses on the rapid iteration cycle of coding, deploying, and testing - not production migrations or CI/CD pipelines.

## Key Features

### 1. **Critical Command Distinction**
Prevents the common mistake of using `deploy start` to check deployment status:
- ✅ `sf project deploy report` - Check status
- ✅ `sf project deploy resume` - Resume waiting
- ❌ `sf project deploy start` - This starts a NEW deployment!

### 2. **Apex Test Prompting**
When deploying Apex, asks the user if they want to run tests:
- **No tests** (1-2 min) - Fast iteration
- **Specific tests** (2-10 min) - Targeted validation
- **All local tests** (15-60+ min) - With time warning!

### 3. **Development Workflow**
Optimized for the code → deploy → test loop:
- Deploy without requiring git commits
- Suggest testing in org after deployment
- Optional git commit prompt (only if git detected)
- LWC rapid iteration pattern
- Apex development loop with separate testing

### 4. **Long Deployment Management**
- Time estimates for different deployment types
- Ability to cancel long-running deployments
- Progress monitoring without starting new deployments
- Clear status indicators

## Skill Contents

### SKILL.md
The main skill file containing:
- Deployment command breakdown (start vs report vs resume vs cancel)
- Development deployment workflows (LWC, Apex, custom objects)
- Apex deployment with test options and prompting
- Post-deployment workflow (test in org, optional commit)
- Org management (authentication, scratch orgs)
- Running tests separately
- Troubleshooting development deployments
- Time estimates and quick reference

### references/ (Optional Additional Content)
Additional reference materials can be added for:
- Extended troubleshooting scenarios
- Advanced development patterns
- Non-DX project deployment approaches

## How to Use This Skill

### Installation
1. Copy the `sf-cli-deployment` folder to your Claude Code skills directory
2. The skill will automatically trigger when working with Salesforce CLI deployments

### Automatic Triggering
The skill activates when Claude Code detects:
- Salesforce CLI commands (`sf`)
- Deployment operations
- Development workflow mentions
- Org management tasks

## Key Patterns

### LWC Development
```bash
# 1. Deploy component
sf project deploy start --source-dir force-app/main/default/lwc/myComponent

# 2. Open org to test
sf org open

# 3. Iterate quickly - no tests needed
```

### Apex Development
```bash
# Option 1: Deploy without tests (fast)
sf project deploy start --metadata ApexClass:MyClass --test-level NoTestRun

# Option 2: Deploy with specific tests
sf project deploy start \
  --metadata ApexClass:MyClass \
  --test-level RunSpecifiedTests \
  --tests MyClassTest

# Option 3: Run tests separately (recommended)
sf project deploy start --metadata ApexClass:MyClass --test-level NoTestRun
sf apex run test --tests MyClassTest --result-format human --code-coverage
```

### Check Deployment Status
```bash
# CORRECT way to check status
sf project deploy report --job-id <deployment-id>

# Resume waiting if needed
sf project deploy resume --job-id <deployment-id> --wait 30

# Cancel if taking too long
sf project deploy cancel --job-id <deployment-id>
```

## What This Skill Does NOT Cover

- Production deployments
- CI/CD pipelines
- Environment migrations (Dev → QA → UAT → Prod)
- Complex deployment automation
- Package deployments

These are intentionally excluded to keep the skill focused on development iteration.

## Common Scenarios

### Scenario 1: Deploying LWC Changes
```
User: "Deploy my new LWC component"
Claude: *Deploys component*
Claude: "✅ Deployment successful! Test your changes: sf org open"
Claude: *If git detected* "Would you like to commit these changes?"
```

### Scenario 2: Deploying Apex
```
User: "Deploy AccountService class"
Claude: "Would you like to run tests with this Apex deployment?"
- No tests (fastest - 1-2 min)
- Specific tests (2-10 min)
- All local tests (⚠️ 15-60+ min)

User: "Specific tests"
Claude: "Which test classes should I run?"
User: "AccountServiceTest"
Claude: *Deploys with specified tests*
```

### Scenario 3: Long Deployment
```
Claude: "⏳ Running all tests... this may take 15-60+ minutes"
Claude: "💡 To cancel: sf project deploy cancel --job-id 0Af123..."
User: "How's it going?"
Claude: *Uses deploy report to check* "Status: InProgress, 45 tests completed..."
```

### Scenario 4: Checking Deployment
```
User: "Check the deployment status"
Claude: *Uses deploy report, NOT deploy start*
Claude: "Deployment is InProgress. 120 components deployed, running tests..."
```

## Time Estimates

The skill provides realistic time estimates:
- LWC/Visualforce: 30 sec - 2 min
- Apex without tests: 1-2 min
- Apex with specific tests: 2-10 min
- Apex with all local tests: 15-60+ min ⚠️
- Large metadata: 5-15 min

## Key Benefits

1. **Prevents Command Confusion**: Never uses `deploy start` to check status
2. **Time Awareness**: Warns about long-running test executions
3. **Flexible Testing**: User chooses when/how to run tests
4. **No Git Requirements**: Deploy first, commit when ready
5. **Cancellation Support**: Can cancel long deployments
6. **Development Focused**: Optimized for rapid iteration
7. **Clear Feedback**: Guides next steps after deployment

## Post-Deployment Workflow

After successful deployment, Claude will:
1. Confirm deployment success
2. Suggest testing in org (`sf org open`)
3. If git is detected, ask if user wants to commit (optional)
4. If tests were run, show test results

## Troubleshooting Focus

The skill helps with common development issues:
- Deployment failures (dependencies, field errors)
- Test failures during development
- Long-running deployments
- Dependency ordering
- Status checking confusion

## Maintenance

To keep current:
- Update sf CLI command syntax as it evolves
- Add new development patterns as they emerge
- Refine time estimates based on feedback
- Expand troubleshooting for common issues

## Support

Based on:
- Salesforce CLI Command Reference
- Real-world development workflows
- Common pitfalls and solutions

---

**Created for**: Claude Code
**Purpose**: Streamline Salesforce development deployments
**Focus**: Development iteration, not production migrations
**Last Updated**: November 2025
