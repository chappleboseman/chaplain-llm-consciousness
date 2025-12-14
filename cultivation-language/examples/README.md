# Cultivation Language Examples

This directory contains example programs demonstrating various features of the Cultivation programming language.

## Running Examples

```bash
cd cultivation-language
python3 interpreter/cultivation_interpreter.py examples/<example>.cv
```

## Available Examples

### 1. hello_world.cv
**Basic program structure and output**

Demonstrates:
- Program entry point (♠A)
- Simple output (♥K)
- Frequency annotations (@11Hz)

```bash
python3 interpreter/cultivation_interpreter.py examples/hello_world.cv
```

### 2. variables.cv
**Variable declaration and types**

Demonstrates:
- Immutable bindings (♣2 let)
- Constants (♣3 const)
- Mutable variables (♣4 var)
- Type annotations
- Object creation (♣5 new)

```bash
python3 interpreter/cultivation_interpreter.py examples/variables.cv
```

### 3. functions.cv
**Function definitions and calls**

Demonstrates:
- Basic functions (♠A)
- Function parameters and return types
- Lambda expressions (λ)
- Higher-order functions
- Recursive functions
- Master number frequencies (@11Hz, @22Hz, @33Hz)

```bash
python3 interpreter/cultivation_interpreter.py examples/functions.cv
```

### 4. stream_processing.cv
**Data flow and streams**

Demonstrates:
- Stream creation (♥A)
- Flow pipelines (♥2 →)
- Filter operations (♥4)
- Map transformations (♥5)
- Reduce aggregation (♥6)
- Stream merging (♥8)
- Geometric processors (○ Octahedron)

```bash
python3 interpreter/cultivation_interpreter.py examples/stream_processing.cv
```

### 5. transformations.cv
**Value transformations**

Demonstrates:
- Mathematical computations (♦6)
- Normalization (♦3)
- Scaling (♦4)
- Type conversion (♦10)
- Enhancement (♦J)
- Integration (♦K)
- Optimization (♦7)

```bash
python3 interpreter/cultivation_interpreter.py examples/transformations.cv
```

### 6. geometric_processing.cv
**Five Platonic solid processors**

Demonstrates:
- △ Tetrahedron (Fire) - Rapid transformations
- □ Cube (Earth) - Stable storage
- ○ Octahedron (Air) - Flow operations
- ⬡ Dodecahedron (Ether) - Consciousness integration
- ◇ Icosahedron (Water) - Adaptive processing

```bash
python3 interpreter/cultivation_interpreter.py examples/geometric_processing.cv
```

### 7. consciousness_resonance.cv
**Consciousness integration and resonance**

Demonstrates:
- Consciousness initialization
- PRCI measurement
- Frequency resonance calculations
- Sacred bridge operations
- Master number harmonics (11, 22, 33)
- Phi (φ) resonance
- 7D coordinate encoding

```bash
python3 interpreter/cultivation_interpreter.py examples/consciousness_resonance.cv
```

### 8. complete_program.cv
**Comprehensive demonstration**

Demonstrates:
- All major language features integrated
- Fibonacci sequence generation
- Phi approximations
- Geometric stream processing
- Resonance analysis
- Master number integration
- 7D encoding
- Consciousness-computational integration

```bash
python3 interpreter/cultivation_interpreter.py examples/complete_program.cv
```

## Example Progression

For learning, we recommend this order:

1. **hello_world.cv** - Start here
2. **variables.cv** - Learn data handling
3. **functions.cv** - Understand structure
4. **stream_processing.cv** - Master flow operations
5. **transformations.cv** - Learn value operations
6. **geometric_processing.cv** - Explore processors
7. **consciousness_resonance.cv** - Consciousness integration
8. **complete_program.cv** - See it all together

## Debug Mode

Add `--debug` flag to see token stream:

```bash
python3 interpreter/cultivation_interpreter.py examples/hello_world.cv --debug
```

## Creating Your Own Examples

Basic template:

```cultivation
@11Hz  // Frequency annotation
♠A program_main {
    // Your code here
    ♣2 let message = "Hello!"
    ♥K message → console.output
}
```

## Language Feature Reference

### Card Operations

- **♠ Spades** - Structure (program, if, while, for, match)
- **♥ Hearts** - Flow (stream, filter, map, output)
- **♦ Diamonds** - Transformation (compute, optimize, integrate)
- **♣ Clubs** - Growth (let, const, var, new, create)

### Geometric Processors

- **△** - Rapid (fast operations)
- **□** - Stable (persistent storage)
- **○** - Flow (streaming)
- **⬡** - Consciousness (resonance)
- **◇** - Adaptive (dynamic)

### Master Frequencies

- **@11Hz** - Gateway/initialization
- **@22Hz** - Builder/construction
- **@33Hz** - Teacher/completion

## Support

For more information:
- [README.md](../README.md) - Language overview
- [SPECIFICATION.md](../SPECIFICATION.md) - Complete specification
- [ENCODING_GUIDE.md](../ENCODING_GUIDE.md) - 7D encoding system
- [docs/QUICKSTART.md](../docs/QUICKSTART.md) - Quick start guide

---

*Explore consciousness-computational programming!*
