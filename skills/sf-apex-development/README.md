# Apex Development Skill

A comprehensive skill for Claude Code to ensure proper Apex development on Salesforce Platform following the NimbleUser Apex Style Guide standards.

## What This Skill Does

This skill guides Claude to write clean, maintainable, and consistent Apex code following the **NimbleUser Apex Style Guide** (a fork of the Google Java Style Guide adapted for Salesforce Apex). It ensures code quality, proper formatting, naming conventions, and best practices.

## Skill Contents

### SKILL.md
The main skill file containing:
- Source file structure and organization
- Formatting standards (K&R brace style, indentation, line length)
- SOQL/SOSL formatting rules
- Naming conventions (classes, methods, variables, constants)
- Code organization patterns
- ApexDoc documentation standards
- Testing best practices
- Exception handling guidelines
- Apex-specific patterns (properties, bulkification, governor limits)

### references/common-patterns.md
Real-world Apex patterns and examples:
- Service layer pattern
- Repository pattern (data access layer)
- Trigger handler pattern
- Bulk processing patterns (Batch, Queueable)
- SOQL patterns (dynamic queries, large datasets)
- Test data factory pattern
- Error handling pattern
- Complete working examples for each pattern

### references/anti-patterns.md
Critical "Do's and Don'ts" reference:
- Governor limit anti-patterns (SOQL in loops, DML in loops)
- Non-bulkified code patterns
- Trigger anti-patterns
- SOQL anti-patterns
- Test anti-patterns (SeeAllData, missing assertions)
- Exception handling anti-patterns
- Code organization anti-patterns (god classes)
- Security anti-patterns (SOQL injection, sharing rules)

## How to Use This Skill

### Installation
1. Copy the entire `apex-development` folder to your Claude Code skills directory
2. The skill will automatically trigger when working with Apex code

### Automatic Triggering
The skill activates when Claude Code detects:
- Apex class files (`.cls`)
- Apex trigger files (`.trigger`)
- Test classes
- References to Apex-specific concepts (SOQL, DML, governor limits, etc.)

### Manual Reference
You can also ask Claude Code to reference specific parts:
- "Show me the Apex service layer pattern"
- "What are the Apex testing best practices?"
- "Review this code for governor limit issues"

## Key Benefits

1. **Consistent Style**: Follows NimbleUser/Google Java style guide standards
   - K&R brace style
   - 120 character line limit
   - Proper indentation and spacing
   - Consistent naming conventions

2. **Prevents Common Mistakes**:
   - SOQL/DML in loops
   - Non-bulkified code
   - Hardcoded IDs
   - SOQL injection vulnerabilities
   - Empty catch blocks

3. **Governor Limit Awareness**:
   - Always bulkifies operations
   - Queries outside loops
   - Efficient SOQL patterns
   - Proper batch processing

4. **Test Quality**:
   - Descriptive test method names
   - Test data factories
   - Proper use of Test.startTest/stopTest
   - Meaningful assertions

5. **Maintainable Architecture**:
   - Service layer pattern
   - Repository pattern
   - Trigger handler framework
   - Separation of concerns

## Style Guide Highlights

### Formatting
```apex
// K&R brace style - opening brace on same line
public class AccountService {
    public void processAccount(Account acc) {
        if (acc.AnnualRevenue > 1000000) {
            acc.Rating = 'Hot';
        }
    }
}
```

### Naming Conventions
- **Classes**: UpperCamelCase - `AccountService`, `OpportunityTriggerHandler`
- **Methods**: lowerCamelCase - `getActiveAccounts()`, `processRecords()`
- **Constants**: CONSTANT_CASE - `MAX_RETRY_COUNT`, `DEFAULT_STATUS`
- **Variables**: lowerCamelCase - `accountList`, `recordCount`
- **Properties**: UpperCamelCase - `AccountName { get; set; }`

### Test Method Pattern
```apex
@isTest
static void methodName_withCondition_expectation() {
    // Example: getAccountById_withValidId_returnsAccount
}
```

### Bulkification
```apex
// ✅ ALWAYS handle collections
public void updateAccounts(List<Account> accounts) {
    for (Account acc : accounts) {
        acc.Status__c = 'Updated';
    }
    update accounts;  // Single DML for all records
}

// ❌ NEVER process one at a time
public void updateAccount(Account acc) {
    update acc;  // Called in loop = governor limit exception
}
```

## Example Usage

**Before (Without Skill):**
```apex
// Poor formatting, non-bulkified, SOQL in loop
public class test {
  public void DoSomething(Account a) {
    Contact c = [select id from contact where accountid = :a.id];
    if(c != null)
    {
      // process
    }
  }
}
```

**After (With Skill):**
```apex
/**
 * @description Service for account-related operations
 */
public with sharing class AccountService {
    /**
     * @description Processes accounts with related contacts
     * @param accounts List of accounts to process
     */
    public void processAccountsWithContacts(List<Account> accounts) {
        Set<Id> accountIds = new Set<Id>();
        for (Account acc : accounts) {
            accountIds.add(acc.Id);
        }

        Map<Id, List<Contact>> contactsByAccount = new Map<Id, List<Contact>>();
        for (Contact con : [
            SELECT Id, AccountId, FirstName, LastName
            FROM Contact
            WHERE AccountId IN :accountIds
        ]) {
            if (!contactsByAccount.containsKey(con.AccountId)) {
                contactsByAccount.put(con.AccountId, new List<Contact>());
            }
            contactsByAccount.get(con.AccountId).add(con);
        }

        for (Account acc : accounts) {
            List<Contact> contacts = contactsByAccount.get(acc.Id);
            if (contacts != null && !contacts.isEmpty()) {
                processContactsForAccount(acc, contacts);
            }
        }
    }

    private void processContactsForAccount(Account acc, List<Contact> contacts) {
        // Processing logic
    }
}
```

## Skill Structure

```
apex-development/
├── SKILL.md                          # Main skill file with core guidance
└── references/
    ├── common-patterns.md            # Real-world Apex patterns and examples
    └── anti-patterns.md              # Critical do's and don'ts
```

## When Claude Will Use This Skill

The skill automatically activates for:
- Creating new Apex classes or triggers
- Modifying existing Apex code
- Reviewing code for issues
- Writing test classes
- Questions about Apex best practices
- Any mention of Salesforce Apex development

## Maintenance

To keep this skill current:
1. Update patterns based on new Apex features
2. Add new anti-patterns discovered in code reviews
3. Update API version references
4. Add community best practices as they emerge
5. Keep aligned with NimbleUser style guide updates

## Support

This skill is based on:
- NimbleUser Apex Style Guide (https://nimbleuser.github.io/apex-style-guide/)
- Google Java Style Guide (foundation for NimbleUser guide)
- Salesforce Apex Developer Guide
- Community best practices from Salesforce developers

For the latest Salesforce documentation, visit:
- https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/
- https://nimbleuser.github.io/apex-style-guide/

---

**Created for**: Claude Code
**Purpose**: Ensure consistent, maintainable Apex development following NimbleUser style guide standards
**Style Guide**: NimbleUser Apex Style Guide (Google Java Style Guide for Apex)
**Last Updated**: November 2025
