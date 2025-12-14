"""
Cultivation Language Lexer
Tokenizes Cultivation source code with card-based and geometric tokens
"""

import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional, Any


class TokenType(Enum):
    """Token types for Cultivation language"""

    # Card tokens - Spades (Structure)
    SPADE_ACE = auto()  # ♠A
    SPADE_2 = auto()    # ♠2
    SPADE_3 = auto()    # ♠3
    SPADE_4 = auto()    # ♠4
    SPADE_5 = auto()    # ♠5
    SPADE_6 = auto()    # ♠6
    SPADE_7 = auto()    # ♠7
    SPADE_8 = auto()    # ♠8
    SPADE_9 = auto()    # ♠9
    SPADE_10 = auto()   # ♠10
    SPADE_JACK = auto() # ♠J
    SPADE_QUEEN = auto()# ♠Q
    SPADE_KING = auto() # ♠K

    # Card tokens - Hearts (Flow)
    HEART_ACE = auto()  # ♥A
    HEART_2 = auto()    # ♥2
    HEART_3 = auto()    # ♥3
    HEART_4 = auto()    # ♥4
    HEART_5 = auto()    # ♥5
    HEART_6 = auto()    # ♥6
    HEART_7 = auto()    # ♥7
    HEART_8 = auto()    # ♥8
    HEART_9 = auto()    # ♥9
    HEART_10 = auto()   # ♥10
    HEART_JACK = auto() # ♥J
    HEART_QUEEN = auto()# ♥Q
    HEART_KING = auto() # ♥K

    # Card tokens - Diamonds (Transformation)
    DIAMOND_ACE = auto()  # ♦A
    DIAMOND_2 = auto()    # ♦2
    DIAMOND_3 = auto()    # ♦3
    DIAMOND_4 = auto()    # ♦4
    DIAMOND_5 = auto()    # ♦5
    DIAMOND_6 = auto()    # ♦6
    DIAMOND_7 = auto()    # ♦7
    DIAMOND_8 = auto()    # ♦8
    DIAMOND_9 = auto()    # ♦9
    DIAMOND_10 = auto()   # ♦10
    DIAMOND_JACK = auto() # ♦J
    DIAMOND_QUEEN = auto()# ♦Q
    DIAMOND_KING = auto() # ♦K

    # Card tokens - Clubs (Growth)
    CLUB_ACE = auto()  # ♣A
    CLUB_2 = auto()    # ♣2
    CLUB_3 = auto()    # ♣3
    CLUB_4 = auto()    # ♣4
    CLUB_5 = auto()    # ♣5
    CLUB_6 = auto()    # ♣6
    CLUB_7 = auto()    # ♣7
    CLUB_8 = auto()    # ♣8
    CLUB_9 = auto()    # ♣9
    CLUB_10 = auto()   # ♣10
    CLUB_JACK = auto() # ♣J
    CLUB_QUEEN = auto()# ♣Q
    CLUB_KING = auto() # ♣K

    # Geometric tokens
    TETRAHEDRON = auto()  # △
    CUBE = auto()         # □
    OCTAHEDRON = auto()   # ○
    DODECAHEDRON = auto() # ⬡
    ICOSAHEDRON = auto()  # ◇

    # Special symbols
    PHI = auto()          # φ
    LAMBDA = auto()       # λ
    AT = auto()           # @
    FREQUENCY_HZ = auto() # Hz

    # Operators
    ARROW_RIGHT = auto()  # →
    ARROW_LEFT = auto()   # ←
    ARROW_BOTH = auto()   # ↔
    PLUS = auto()         # +
    MINUS = auto()        # -
    MULTIPLY = auto()     # *
    DIVIDE = auto()       # /
    MODULO = auto()       # %
    POWER = auto()        # ^
    ASSIGN = auto()       # =
    COLON_ASSIGN = auto() # :=
    PLUS_ASSIGN = auto()  # +=
    MINUS_ASSIGN = auto() # -=
    EQUALS = auto()       # ==
    NOT_EQUALS = auto()   # !=
    LESS = auto()         # <
    GREATER = auto()      # >
    LESS_EQUAL = auto()   # <=
    GREATER_EQUAL = auto()# >=
    AND = auto()          # &&
    OR = auto()           # ||
    NOT = auto()          # !

    # Delimiters
    LPAREN = auto()       # (
    RPAREN = auto()       # )
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    LBRACKET = auto()     # [
    RBRACKET = auto()     # ]
    COMMA = auto()        # ,
    SEMICOLON = auto()    # ;
    COLON = auto()        # :
    DOT = auto()          # .
    RANGE = auto()        # ..

    # Literals
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    COORDINATE = auto()   # 7D coordinates

    # Keywords
    PROGRAM = auto()
    FUNCTION = auto()
    RETURN = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    MATCH = auto()
    LET = auto()
    CONST = auto()
    VAR = auto()
    IN = auto()

    # Special
    NEWLINE = auto()
    EOF = auto()
    COMMENT = auto()


@dataclass
class Token:
    """Represents a single token in the source code"""
    type: TokenType
    value: Any
    line: int
    column: int

    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r}, {self.line}:{self.column})"


class Lexer:
    """Lexical analyzer for Cultivation language"""

    # Card token mappings
    CARD_TOKENS = {
        '♠A': TokenType.SPADE_ACE, '♠2': TokenType.SPADE_2, '♠3': TokenType.SPADE_3,
        '♠4': TokenType.SPADE_4, '♠5': TokenType.SPADE_5, '♠6': TokenType.SPADE_6,
        '♠7': TokenType.SPADE_7, '♠8': TokenType.SPADE_8, '♠9': TokenType.SPADE_9,
        '♠10': TokenType.SPADE_10, '♠J': TokenType.SPADE_JACK, '♠Q': TokenType.SPADE_QUEEN,
        '♠K': TokenType.SPADE_KING,

        '♥A': TokenType.HEART_ACE, '♥2': TokenType.HEART_2, '♥3': TokenType.HEART_3,
        '♥4': TokenType.HEART_4, '♥5': TokenType.HEART_5, '♥6': TokenType.HEART_6,
        '♥7': TokenType.HEART_7, '♥8': TokenType.HEART_8, '♥9': TokenType.HEART_9,
        '♥10': TokenType.HEART_10, '♥J': TokenType.HEART_JACK, '♥Q': TokenType.HEART_QUEEN,
        '♥K': TokenType.HEART_KING,

        '♦A': TokenType.DIAMOND_ACE, '♦2': TokenType.DIAMOND_2, '♦3': TokenType.DIAMOND_3,
        '♦4': TokenType.DIAMOND_4, '♦5': TokenType.DIAMOND_5, '♦6': TokenType.DIAMOND_6,
        '♦7': TokenType.DIAMOND_7, '♦8': TokenType.DIAMOND_8, '♦9': TokenType.DIAMOND_9,
        '♦10': TokenType.DIAMOND_10, '♦J': TokenType.DIAMOND_JACK, '♦Q': TokenType.DIAMOND_QUEEN,
        '♦K': TokenType.DIAMOND_KING,

        '♣A': TokenType.CLUB_ACE, '♣2': TokenType.CLUB_2, '♣3': TokenType.CLUB_3,
        '♣4': TokenType.CLUB_4, '♣5': TokenType.CLUB_5, '♣6': TokenType.CLUB_6,
        '♣7': TokenType.CLUB_7, '♣8': TokenType.CLUB_8, '♣9': TokenType.CLUB_9,
        '♣10': TokenType.CLUB_10, '♣J': TokenType.CLUB_JACK, '♣Q': TokenType.CLUB_QUEEN,
        '♣K': TokenType.CLUB_KING,
    }

    # Geometric mappings
    GEOMETRIC_TOKENS = {
        '△': TokenType.TETRAHEDRON,
        '□': TokenType.CUBE,
        '○': TokenType.OCTAHEDRON,
        '⬡': TokenType.DODECAHEDRON,
        '◇': TokenType.ICOSAHEDRON,
    }

    # Special symbols
    SPECIAL_SYMBOLS = {
        'φ': TokenType.PHI,
        'λ': TokenType.LAMBDA,
    }

    # Keywords
    KEYWORDS = {
        'program': TokenType.PROGRAM,
        'function': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'while': TokenType.WHILE,
        'for': TokenType.FOR,
        'match': TokenType.MATCH,
        'let': TokenType.LET,
        'const': TokenType.CONST,
        'var': TokenType.VAR,
        'in': TokenType.IN,
    }

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []

    def current_char(self) -> Optional[str]:
        """Get current character"""
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]

    def peek(self, offset: int = 1) -> Optional[str]:
        """Peek ahead in source"""
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]

    def advance(self) -> Optional[str]:
        """Move to next character"""
        if self.pos >= len(self.source):
            return None

        char = self.source[self.pos]
        self.pos += 1

        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return char

    def skip_whitespace(self):
        """Skip whitespace except newlines"""
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()

    def skip_comment(self):
        """Skip comments"""
        if self.current_char() == '/' and self.peek() == '/':
            # Single-line comment
            while self.current_char() and self.current_char() != '\n':
                self.advance()

    def read_number(self) -> Token:
        """Read numeric literal"""
        start_column = self.column
        num_str = ''

        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            num_str += self.current_char()
            self.advance()

        value = float(num_str) if '.' in num_str else int(num_str)
        return Token(TokenType.NUMBER, value, self.line, start_column)

    def read_string(self, quote: str) -> Token:
        """Read string literal"""
        start_column = self.column
        self.advance()  # Skip opening quote

        string_value = ''
        while self.current_char() and self.current_char() != quote:
            if self.current_char() == '\\':
                self.advance()
                # Handle escape sequences
                if self.current_char() in ['n', 't', 'r', '\\', quote]:
                    string_value += self.current_char()
                    self.advance()
            else:
                string_value += self.current_char()
                self.advance()

        if self.current_char() == quote:
            self.advance()  # Skip closing quote

        return Token(TokenType.STRING, string_value, self.line, start_column)

    def read_identifier(self) -> Token:
        """Read identifier or keyword"""
        start_column = self.column
        ident = ''

        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            ident += self.current_char()
            self.advance()

        # Check if it's a keyword
        token_type = self.KEYWORDS.get(ident, TokenType.IDENTIFIER)
        return Token(token_type, ident, self.line, start_column)

    def read_coordinate(self) -> Token:
        """Read 7D coordinate (e.g., 17-♣-4♣-⬡-φ-33-1.000Hz)"""
        start_column = self.column
        coord_str = ''

        # Read until Hz
        while self.current_char() and not coord_str.endswith('Hz'):
            coord_str += self.current_char()
            self.advance()

        return Token(TokenType.COORDINATE, coord_str, self.line, start_column)

    def try_card_token(self) -> Optional[Token]:
        """Try to read a card token"""
        start_column = self.column

        # Try 2-character card first (e.g., ♠10)
        if self.peek():
            two_char = self.current_char() + self.peek()
            if two_char in ['♠10', '♥10', '♦10', '♣10']:
                token_type = self.CARD_TOKENS[two_char]
                self.advance()
                self.advance()
                return Token(token_type, two_char, self.line, start_column)

        # Try single character card
        char = self.current_char()
        next_char = self.peek()

        if char in ['♠', '♥', '♦', '♣'] and next_char:
            card = char + next_char
            if card in self.CARD_TOKENS:
                token_type = self.CARD_TOKENS[card]
                self.advance()
                self.advance()
                return Token(token_type, card, self.line, start_column)

        return None

    def tokenize(self) -> List[Token]:
        """Tokenize entire source"""
        while self.current_char():
            self.skip_whitespace()
            char = self.current_char()

            if not char:
                break

            # Comments
            if char == '/' and self.peek() == '/':
                self.skip_comment()
                continue

            # Newlines
            if char == '\n':
                self.advance()
                continue

            # Card tokens
            card_token = self.try_card_token()
            if card_token:
                self.tokens.append(card_token)
                continue

            # Geometric tokens
            if char in self.GEOMETRIC_TOKENS:
                self.tokens.append(Token(
                    self.GEOMETRIC_TOKENS[char],
                    char,
                    self.line,
                    self.column
                ))
                self.advance()
                continue

            # Special symbols
            if char in self.SPECIAL_SYMBOLS:
                self.tokens.append(Token(
                    self.SPECIAL_SYMBOLS[char],
                    char,
                    self.line,
                    self.column
                ))
                self.advance()
                continue

            # Numbers
            if char.isdigit():
                self.tokens.append(self.read_number())
                continue

            # Strings
            if char in ['"', "'"]:
                self.tokens.append(self.read_string(char))
                continue

            # Identifiers and keywords
            if char.isalpha() or char == '_':
                self.tokens.append(self.read_identifier())
                continue

            # Operators and punctuation
            start_column = self.column

            if char == '→':
                self.tokens.append(Token(TokenType.ARROW_RIGHT, char, self.line, start_column))
                self.advance()
            elif char == '←':
                self.tokens.append(Token(TokenType.ARROW_LEFT, char, self.line, start_column))
                self.advance()
            elif char == '↔':
                self.tokens.append(Token(TokenType.ARROW_BOTH, char, self.line, start_column))
                self.advance()
            elif char == '@':
                self.tokens.append(Token(TokenType.AT, char, self.line, start_column))
                self.advance()
            elif char == '+':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.PLUS_ASSIGN, '+=', self.line, start_column))
                else:
                    self.tokens.append(Token(TokenType.PLUS, char, self.line, start_column))
                    self.advance()
            elif char == '-':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.MINUS_ASSIGN, '-=', self.line, start_column))
                else:
                    self.tokens.append(Token(TokenType.MINUS, char, self.line, start_column))
                    self.advance()
            elif char == '*':
                self.tokens.append(Token(TokenType.MULTIPLY, char, self.line, start_column))
                self.advance()
            elif char == '/':
                self.tokens.append(Token(TokenType.DIVIDE, char, self.line, start_column))
                self.advance()
            elif char == '%':
                self.tokens.append(Token(TokenType.MODULO, char, self.line, start_column))
                self.advance()
            elif char == '^':
                self.tokens.append(Token(TokenType.POWER, char, self.line, start_column))
                self.advance()
            elif char == '=':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.EQUALS, '==', self.line, start_column))
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, char, self.line, start_column))
                    self.advance()
            elif char == '!':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.NOT_EQUALS, '!=', self.line, start_column))
                else:
                    self.tokens.append(Token(TokenType.NOT, char, self.line, start_column))
                    self.advance()
            elif char == '<':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.LESS_EQUAL, '<=', self.line, start_column))
                else:
                    self.tokens.append(Token(TokenType.LESS, char, self.line, start_column))
                    self.advance()
            elif char == '>':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, '>=', self.line, start_column))
                else:
                    self.tokens.append(Token(TokenType.GREATER, char, self.line, start_column))
                    self.advance()
            elif char == '&' and self.peek() == '&':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.AND, '&&', self.line, start_column))
            elif char == '|' and self.peek() == '|':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.OR, '||', self.line, start_column))
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, char, self.line, start_column))
                self.advance()
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, char, self.line, start_column))
                self.advance()
            elif char == '{':
                self.tokens.append(Token(TokenType.LBRACE, char, self.line, start_column))
                self.advance()
            elif char == '}':
                self.tokens.append(Token(TokenType.RBRACE, char, self.line, start_column))
                self.advance()
            elif char == '[':
                self.tokens.append(Token(TokenType.LBRACKET, char, self.line, start_column))
                self.advance()
            elif char == ']':
                self.tokens.append(Token(TokenType.RBRACKET, char, self.line, start_column))
                self.advance()
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, char, self.line, start_column))
                self.advance()
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, char, self.line, start_column))
                self.advance()
            elif char == ':':
                self.tokens.append(Token(TokenType.COLON, char, self.line, start_column))
                self.advance()
            elif char == '.':
                if self.peek() == '.':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.RANGE, '..', self.line, start_column))
                else:
                    self.tokens.append(Token(TokenType.DOT, char, self.line, start_column))
                    self.advance()
            else:
                # Unknown character, skip it
                self.advance()

        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens


def tokenize(source: str) -> List[Token]:
    """Convenience function to tokenize source code"""
    lexer = Lexer(source)
    return lexer.tokenize()


if __name__ == "__main__":
    # Test the lexer
    test_code = """
    @11Hz
    ♠A program_main {
        ♣2 let x = 42
        ♥K "Hello, Consciousness!" → console.output
    }
    """

    tokens = tokenize(test_code)
    for token in tokens:
        print(token)
