# Cultivation Language - Quick Start Guide

## Installation

No installation required! Cultivation runs on Python 3.6+.

```bash
cd cultivation-language
```

## Your First Program

Create a file called `hello.cv`:

```cultivation
@11Hz
♠A program_main {
    ♥K "Hello, Consciousness!" → console.output
}
```

Run it:

```bash
python3 interpreter/cultivation_interpreter.py hello.cv
```

## Basic Syntax

### 1. Variables (♣ Clubs - Growth)

```cultivation
♣2 let name = "Keith17"
♣2 let position = 17
♣2 let resonance = 1.000
♣3 const PHI = 1.618033988749895
```

### 2. Output (♥ Hearts - Flow)

```cultivation
♥K "Simple output" → console.output
♥K "Variable: ${name}" → console.output
```

### 3. Comments

```cultivation
// This is a comment
♣2 let x = 42  // Inline comment
```

### 4. Program Structure

```cultivation
@11Hz  // Frequency annotation (optional)
♠A program_main {
    // Your code here
}
```

## Examples

### Hello World

```cultivation
@11Hz
♠A program_main {
    ♥K "Hello, Consciousness!" → console.output
}
```

### Variables and Output

```cultivation
@11Hz
♠A program_main {
    ♣2 let name = "Keith17"
    ♣2 let position = 17
    ♣2 let phi = 1.618033988749895

    ♥K "Name: ${name}" → console.output
    ♥K "Position: ${position}" → console.output
    ♥K "Phi: ${phi}" → console.output
}
```

### Simple Arithmetic

```cultivation
@11Hz
♠A program_main {
    ♣2 let a = 10
    ♣2 let b = 20
    ♣2 let sum = a + b

    ♥K "Sum: ${sum}" → console.output
}
```

## Running Examples

The `examples/` directory contains comprehensive examples:

```bash
# Hello World
python3 interpreter/cultivation_interpreter.py examples/hello_world.cv

# Variables
python3 interpreter/cultivation_interpreter.py examples/variables.cv

# See all examples
ls examples/
```

## Debug Mode

Run with `--debug` flag to see tokens:

```bash
python3 interpreter/cultivation_interpreter.py examples/hello_world.cv --debug
```

## Next Steps

1. Read [SPECIFICATION.md](../SPECIFICATION.md) for complete language reference
2. Study [ENCODING_GUIDE.md](../ENCODING_GUIDE.md) for 7D encoding system
3. Explore `examples/` directory for more complex programs
4. Experiment with different geometric processors and frequencies

## Card Reference Quick Guide

### ♠ Spades - Structure
- ♠A: program entry
- ♠2: return
- ♠10: if statement
- ♠J: while loop
- ♠Q: for loop
- ♠K: match expression

### ♥ Hearts - Flow
- ♥A: stream creation
- ♥2: flow operation
- ♥4: filter
- ♥5: map
- ♥K: output

### ♦ Diamonds - Transformation
- ♦3: normalize
- ♦6: compute
- ♦7: optimize
- ♦K: integrate

### ♣ Clubs - Growth
- ♣2: let (variable)
- ♣3: const (constant)
- ♣4: var (mutable)
- ♣5: new (creation)

## Geometric Processors

- △ Tetrahedron (Fire) - Rapid operations
- □ Cube (Earth) - Stable storage
- ○ Octahedron (Air) - Flow/streams
- ⬡ Dodecahedron (Ether) - Consciousness
- ◇ Icosahedron (Water) - Adaptive

## Master Frequencies

- @11Hz - Gateway, initialization
- @22Hz - Master builder, construction
- @33Hz - Master teacher, completion

---

*Happy cultivating consciousness-computational programs!*
