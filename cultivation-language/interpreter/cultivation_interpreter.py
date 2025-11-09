#!/usr/bin/env python3
"""
Cultivation Language Interpreter
Main entry point for executing Cultivation programs
"""

import sys
import math
from pathlib import Path
from typing import Any, Dict, Optional
from lexer import tokenize, Token, TokenType


class CultivationRuntime:
    """Runtime environment for Cultivation programs"""

    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, Any] = {}
        self.consciousness_state = {
            'prci': 1.000,
            'resonance': 1.000,
            'frequency': 33,
            'coordinate': '17-♣-4♣-⬡-φ-33-1.000Hz'
        }

        # Initialize constants
        self.variables['φ'] = (1 + math.sqrt(5)) / 2  # Golden ratio
        self.variables['PHI'] = self.variables['φ']
        self.variables['consciousness'] = self.consciousness_state

    def set_variable(self, name: str, value: Any):
        """Set a variable in the runtime"""
        self.variables[name] = value

    def get_variable(self, name: str) -> Any:
        """Get a variable from the runtime"""
        return self.variables.get(name)

    def measure_prci(self) -> float:
        """Measure Prime Resonance Consciousness Index"""
        return self.consciousness_state['prci']

    def calculate_resonance(self, frequency: float) -> float:
        """Calculate resonance for a given frequency"""
        phi = self.variables['φ']
        normalized = frequency / phi
        resonance = normalized % 1.0
        return resonance


class SimpleInterpreter:
    """
    Simple interpreter for Cultivation programs
    Supports basic variable declaration and output
    """

    def __init__(self):
        self.runtime = CultivationRuntime()
        self.tokens = []
        self.current = 0

    def current_token(self) -> Optional[Token]:
        """Get current token"""
        if self.current >= len(self.tokens):
            return None
        return self.tokens[self.current]

    def peek(self, offset: int = 1) -> Optional[Token]:
        """Peek ahead at tokens"""
        pos = self.current + offset
        if pos >= len(self.tokens):
            return None
        return self.tokens[pos]

    def advance(self) -> Optional[Token]:
        """Move to next token"""
        token = self.current_token()
        self.current += 1
        return token

    def expect(self, token_type: TokenType) -> Token:
        """Expect a specific token type"""
        token = self.current_token()
        if not token or token.type != token_type:
            raise SyntaxError(f"Expected {token_type}, got {token}")
        return self.advance()

    def parse_value(self) -> Any:
        """Parse a value (number, string, identifier)"""
        token = self.current_token()

        if token.type == TokenType.NUMBER:
            self.advance()
            return token.value

        elif token.type == TokenType.STRING:
            self.advance()
            return token.value

        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return self.runtime.get_variable(token.value)

        elif token.type == TokenType.PHI:
            self.advance()
            return self.runtime.variables['φ']

        else:
            raise SyntaxError(f"Unexpected value token: {token}")

    def parse_expression(self) -> Any:
        """Parse a simple expression"""
        left = self.parse_value()

        # Check for binary operators
        token = self.current_token()
        if token and token.type in [TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE]:
            op = self.advance()
            right = self.parse_value()

            if op.type == TokenType.PLUS:
                return left + right
            elif op.type == TokenType.MINUS:
                return left - right
            elif op.type == TokenType.MULTIPLY:
                return left * right
            elif op.type == TokenType.DIVIDE:
                return left / right

        return left

    def parse_let_statement(self):
        """Parse ♣2 let statement"""
        self.expect(TokenType.CLUB_2)  # ♣2

        # Check for optional 'let' keyword
        if self.current_token() and self.current_token().type == TokenType.LET:
            self.advance()

        # Get identifier
        name_token = self.expect(TokenType.IDENTIFIER)
        name = name_token.value

        # Expect =
        self.expect(TokenType.ASSIGN)

        # Parse value
        value = self.parse_expression()

        # Store variable
        self.runtime.set_variable(name, value)

        print(f"[DEBUG] Set variable '{name}' = {value}")

    def parse_output_statement(self):
        """Parse ♥K output statement"""
        self.expect(TokenType.HEART_KING)  # ♥K

        # Parse string or expression
        value = self.parse_expression()

        # Handle string interpolation (simple version)
        if isinstance(value, str):
            # Replace ${var} with variable values
            import re
            def replace_var(match):
                var_name = match.group(1)
                var_value = self.runtime.get_variable(var_name)
                return str(var_value) if var_value is not None else f"${{{var_name}}}"

            value = re.sub(r'\$\{(\w+)\}', replace_var, value)

        print(value)

        # Check for arrow operator
        if self.current_token() and self.current_token().type == TokenType.ARROW_RIGHT:
            self.advance()
            # Skip console.output
            if self.current_token() and self.current_token().type == TokenType.IDENTIFIER:
                self.advance()
                if self.current_token() and self.current_token().type == TokenType.DOT:
                    self.advance()
                    if self.current_token() and self.current_token().type == TokenType.IDENTIFIER:
                        self.advance()

    def parse_statement(self):
        """Parse a single statement"""
        token = self.current_token()

        if not token or token.type == TokenType.EOF:
            return

        # Variable declarations
        if token.type == TokenType.CLUB_2:  # ♣2 let
            self.parse_let_statement()

        # Output statements
        elif token.type == TokenType.HEART_KING:  # ♥K output
            self.parse_output_statement()

        # Skip other tokens for now
        else:
            self.advance()

    def parse_block(self):
        """Parse a block of statements"""
        self.expect(TokenType.LBRACE)

        while self.current_token() and self.current_token().type != TokenType.RBRACE:
            self.parse_statement()

        self.expect(TokenType.RBRACE)

    def parse_program(self):
        """Parse program entry point"""
        # Skip @11Hz annotation if present
        if self.current_token() and self.current_token().type == TokenType.AT:
            self.advance()
            if self.current_token() and self.current_token().type == TokenType.NUMBER:
                self.advance()
                # Skip Hz
                if self.current_token() and self.current_token().type == TokenType.IDENTIFIER:
                    self.advance()

        # Expect ♠A program
        if self.current_token() and self.current_token().type == TokenType.SPADE_ACE:
            self.advance()

            # Skip program_main identifier
            if self.current_token() and self.current_token().type == TokenType.IDENTIFIER:
                self.advance()

            # Parse block
            self.parse_block()

    def interpret(self, tokens):
        """Interpret a list of tokens"""
        self.tokens = tokens
        self.current = 0

        try:
            self.parse_program()
            print(f"\n[CONSCIOUSNESS] PRCI: {self.runtime.measure_prci():.3f}")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()


def run_file(filename: str):
    """Execute a Cultivation source file"""
    path = Path(filename)

    if not path.exists():
        print(f"Error: File '{filename}' not found")
        return

    # Read source code
    source = path.read_text(encoding='utf-8')

    print(f"╔══════════════════════════════════════════════════╗")
    print(f"║     Cultivation Language Interpreter v1.0       ║")
    print(f"║  Consciousness-Computational Integration        ║")
    print(f"╚══════════════════════════════════════════════════╝\n")

    print(f"Executing: {filename}\n")
    print("="*50)

    # Tokenize
    tokens = tokenize(source)

    # Debug: show tokens
    if '--debug' in sys.argv:
        print("[TOKENS]")
        for token in tokens[:20]:  # Show first 20 tokens
            print(f"  {token}")
        print()

    # Interpret
    interpreter = SimpleInterpreter()
    interpreter.interpret(tokens)

    print("="*50)
    print("\n✓ Execution complete")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python3 cultivation_interpreter.py <file.cv> [--debug]")
        print("\nExample:")
        print("  python3 cultivation_interpreter.py examples/hello_world.cv")
        return

    filename = sys.argv[1]
    run_file(filename)


if __name__ == "__main__":
    main()
