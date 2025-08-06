import google.generativeai as genai
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class BDDGenerator:
    def __init__(self):
        api_key = os.getenv("GOOGLE_AI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    async def generate_bdd(self, user_story: str, format_style: str = "gherkin") -> str:
        """
        Generate BDD test cases from user story
        
        Args:
            user_story: User story or product requirement description
            format_style: Output format (gherkin, checklist, plain)
            
        Returns:
            Generated BDD test cases as string
        """
        
        system_prompt = f"""You are an expert QA engineer specializing in Behavior Driven Development (BDD). 
Generate comprehensive BDD test cases from user stories and product requirements.

For {format_style} format:
- Use proper Gherkin syntax with Feature, Scenario, Given, When, Then
- Include multiple scenarios covering happy path, edge cases, and error conditions
- Make scenarios specific and testable
- Use clear, business-focused language
- Include Background section when appropriate
- Add proper indentation and formatting

Focus on:
1. Happy path scenarios
2. Edge cases and boundary conditions
3. Error scenarios and negative testing
4. Data-driven scenarios when applicable
5. Accessibility and usability considerations"""

        user_prompt = f"""Generate comprehensive BDD test cases for the following user story:

{user_story}

Requirements:
- Format: {format_style}
- Include multiple scenarios (happy path, edge cases, error conditions)
- Make scenarios specific and testable
- Use clear business language
- Cover all important user flows"""

        try:
            prompt_text = f"{system_prompt}\n\n{user_prompt}"
            response = self.model.generate_content(prompt_text)
            
            if response.text:
                return response.text
            else:
                return self._generate_fallback_bdd(user_story, format_style)
            
        except Exception as e:
            # Fallback to template-based generation if OpenAI fails
            return self._generate_fallback_bdd(user_story, format_style)
    
    def _generate_fallback_bdd(self, user_story: str, format_style: str) -> str:
        """Fallback BDD generation when OpenAI is not available"""
        
        if format_style == "gherkin":
            return f'''Feature: {user_story[:50]}...

  Background:
    Given the user is on the application homepage
    And the application is fully loaded

  Scenario: Happy Path - Successful Operation
    Given the user has valid credentials
    When the user performs the main action
    Then the operation should complete successfully
    And the user should see a success message
    And the system should update accordingly

  Scenario: Edge Case - Invalid Input
    Given the user provides invalid data
    When the user attempts to proceed
    Then the system should display an error message
    And the operation should not complete
    And the user should be able to correct the input

  Scenario: Error Condition - System Failure
    Given the system is experiencing issues
    When the user attempts to perform the action
    Then the system should handle the error gracefully
    And the user should be informed of the issue
    And the system should provide recovery options

  Scenario Outline: Data-Driven Testing
    Given the user has <user_type> access
    When the user performs the action with <input_data>
    Then the result should be <expected_outcome>

    Examples:
      | user_type | input_data | expected_outcome |
      | admin     | valid      | success          |
      | user      | valid      | success          |
      | guest     | valid      | limited_access   |
      | admin     | invalid    | error_message    |'''
        
        elif format_style == "checklist":
            return f'''BDD Test Checklist for: {user_story}

✓ HAPPY PATH TESTS:
  □ [ ] User can successfully complete the main workflow
  □ [ ] All required fields are properly validated
  □ [ ] Success messages are displayed correctly
  □ [ ] System state is updated appropriately
  □ [ ] User can proceed to next step

✓ EDGE CASE TESTS:
  □ [ ] System handles maximum input lengths
  □ [ ] System handles minimum input lengths
  □ [ ] System handles special characters in input
  □ [ ] System handles empty/null values appropriately
  □ [ ] System handles concurrent user actions

✓ ERROR CONDITION TESTS:
  □ [ ] System displays appropriate error messages
  □ [ ] System prevents invalid operations
  □ [ ] System handles network failures gracefully
  □ [ ] System provides recovery options
  □ [ ] System maintains data integrity during errors

✓ ACCESSIBILITY TESTS:
  □ [ ] All elements are keyboard accessible
  □ [ ] Screen readers can interpret all content
  □ [ ] Color contrast meets WCAG guidelines
  □ [ ] Focus indicators are visible
  □ [ ] Alternative text is provided for images

✓ PERFORMANCE TESTS:
  □ [ ] Page loads within acceptable time
  □ [ ] Operations complete within expected duration
  □ [ ] System handles expected user load
  □ [ ] Memory usage remains stable
  □ [ ] No memory leaks during extended use'''
        
        else:  # plain text
            return f'''BDD Test Cases for: {user_story}

1. HAPPY PATH SCENARIOS:
   - User successfully completes the main workflow
   - All validations pass with correct input
   - Success feedback is provided to user
   - System state updates correctly
   - User can proceed to subsequent steps

2. EDGE CASE SCENARIOS:
   - System handles boundary values correctly
   - Special characters are processed properly
   - Empty/null inputs are handled appropriately
   - Maximum/minimum input lengths are validated
   - Concurrent operations don't conflict

3. ERROR SCENARIOS:
   - Invalid inputs are rejected with clear messages
   - System failures are handled gracefully
   - Users can recover from error states
   - Data integrity is maintained during errors
   - Error messages are user-friendly

4. ACCESSIBILITY SCENARIOS:
   - All functionality is keyboard accessible
   - Screen readers can interpret all content
   - Visual design meets accessibility standards
   - Focus management works correctly
   - Alternative input methods are supported

5. PERFORMANCE SCENARIOS:
   - Operations complete within acceptable time
   - System remains responsive under load
   - Memory usage is optimized
   - No performance degradation over time
   - Scalability requirements are met''' 