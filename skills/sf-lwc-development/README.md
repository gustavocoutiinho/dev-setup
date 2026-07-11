# Lightning Web Components Development Skill

A comprehensive skill for Claude Code to ensure proper Lightning Web Component development on Salesforce Platform.

## What This Skill Does

This skill guides Claude to **always use standard Lightning components (`lightning-*` namespace)** instead of generic HTML elements when building Salesforce LWC applications. It solves the common problem where AI tools default to using standard web components instead of Salesforce-specific components.

## Skill Contents

### SKILL.md
The main skill file containing:
- Core principle: Always use Lightning namespace components
- Component selection guide (quick reference tables)
- Essential LWC patterns
- Common anti-patterns to avoid
- Styling with SLDS
- Component communication patterns
- Quick reference for most common components

### references/component-catalog.md
Comprehensive catalog of all Lightning components organized by category:
- Input components (lightning-input, lightning-textarea, lightning-combobox, etc.)
- Button components (lightning-button, lightning-button-icon, etc.)
- Layout components (lightning-card, lightning-layout, lightning-accordion, etc.)
- Data display components (lightning-datatable, lightning-tree, formatted components, etc.)
- Record interaction components (lightning-record-form, lightning-record-edit-form, etc.)
- Navigation and feedback components
- Each component includes: purpose, key attributes, and code examples

### references/common-patterns.md
Real-world LWC patterns and examples:
- Form validation pattern
- Wire service pattern
- Imperative Apex call pattern
- Datatable with row actions
- Navigation patterns
- Parent-child communication
- Conditional rendering
- Refresh data pattern
- Toast notifications
- Modal/popup pattern
- Error handling pattern
- Lifecycle hooks
- And more...

### references/anti-patterns.md
Critical "Do's and Don'ts" reference:
- Component selection anti-patterns (❌ NEVER use generic HTML)
- Data handling anti-patterns
- Validation anti-patterns
- Styling anti-patterns
- Performance anti-patterns
- Security anti-patterns
- Navigation anti-patterns
- Red flags in code reviews
- Decision matrix for component selection
- Checklist before deployment

## How to Use This Skill

### Installation
1. Copy the entire `lwc-development` folder to your Claude Code skills directory
2. The skill will automatically trigger when working with Salesforce/LWC projects

### Automatic Triggering
The skill activates when Claude Code detects:
- Salesforce project mentions
- Lightning Web Components
- `.js-meta.xml` files
- SLDS references
- `lightning-*` component mentions

### Manual Reference
You can also ask Claude Code to reference specific parts:
- "Check the component catalog for the right Lightning component"
- "Show me common LWC patterns for forms"
- "What are the anti-patterns I should avoid?"

## Key Benefits

1. **Ensures Proper Component Usage**: Always uses `lightning-button` instead of `<button>`, `lightning-input` instead of `<input>`, etc.

2. **Salesforce Best Practices**: Follows official Salesforce guidelines for LWC development

3. **Prevents Common Mistakes**: Catches typical errors like:
   - Using generic HTML form elements
   - Manual validation instead of built-in
   - Custom CSS instead of SLDS
   - DOM manipulation instead of property binding

4. **Comprehensive Reference**: Quick access to all Lightning components and their usage

5. **Real-World Examples**: Practical patterns for common scenarios

## Example Usage

**Before (Without Skill):**
```html
<input type="text" placeholder="Name" />
<button onclick={handleClick}>Submit</button>
<select><option>Option 1</option></select>
```

**After (With Skill):**
```html
<lightning-input label="Name"></lightning-input>
<lightning-button label="Submit" onclick={handleClick}></lightning-button>
<lightning-combobox label="Select" options={options}></lightning-combobox>
```

## Skill Structure

```
lwc-development/
├── SKILL.md                              # Main skill file with core guidance
└── references/
    ├── component-catalog.md              # Complete Lightning component reference
    ├── common-patterns.md                # Real-world LWC patterns and examples
    └── anti-patterns.md                  # Critical do's and don'ts
```

## When Claude Will Use This Skill

The skill automatically activates for:
- Creating new Lightning Web Components
- Modifying existing LWC code
- Fixing LWC bugs or issues
- Questions about Salesforce component selection
- Any mention of Lightning, SLDS, or Salesforce Platform development

## Maintenance

To keep this skill current:
1. Update component catalog when new Lightning components are released
2. Add new patterns as they emerge in the community
3. Update anti-patterns based on real-world issues encountered
4. Keep SLDS class references current with new releases

## Support

This skill is based on:
- Official Salesforce Lightning Web Components Developer Guide
- Salesforce Lightning Design System (SLDS)
- Community best practices from Salesforce developers
- Real-world LWC development experience

For the latest Salesforce documentation, visit:
- https://developer.salesforce.com/docs/platform/lwc/overview
- https://developer.salesforce.com/docs/component-library

---

**Created for**: Claude Code
**Purpose**: Ensure proper Lightning Web Component development with standard Salesforce components
**Last Updated**: November 2025
