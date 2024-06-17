# Brainrot

[Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) for Gen Alpha and [@philiphan0109](https://github.com/philiphan0109/). Just like Brainfuck, Brainrot is Turing-complete, so any computer program can theoretically be written in this glorious language.

## Compiler Usage

The Brainrot Interpreter can only run one file at a time. The first and only argument passed to the interpreter is the name of that file. Any file format is accepted by the compiler, so long as it is a readable text file.

You must have python installed.

Run the following command in the terminal to execute a file titled "brainrot.b":
```
python brainrot.py brainrot.b
```

## Language

### Phrases

*Explanations taken from [Wikipedia](https://en.wikipedia.org/wiki/Brainfuck#Language_design)*

| Brainrot Phrase | Brainfuck Symbol | Explanation                                                                                                                                                                          |
|-----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SKIBIDI         | >                | Increment the data pointer by one (to point to the next cell to the right).                                                                                                          |
| TOILET          | <                | Decrement the data pointer by one (to point to the next cell to the left).                                                                                                           |
| SIGMA           | +                | Increment the byte at the data pointer by one.                                                                                                                                       |
| BETA            | -                | Decrement the byte at the data pointer by one.                                                                                                                                       |
| RIZZ            | ,                | Accept one byte of input, storing its value in the byte at the data pointer.                                                                                                         |
| GOON            | .                | Output the byte at the data pointer.                                                                                                                                                 |
| SUS             | [                | If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.    |
| AMOGUS          | ]                | If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.[a] |

All phrases must be typed in CAPITAL LETTERS. Phrases are separated by whitespaces (" ") or new line characters. Tabs ("\t") are not permitted. However, lines may be indented with either whitespaces or tabs ("\t").

Unlike Brainfuck, Brainrot introduces a new comment symbol, GYATT. GYATT and any characters following it on that line are considered comments and ignored.

An unknown phrases will cause the interpreter to raise a syntax error. SUS's without a corresopnding AMOGUS also raise a syntax error. If you try to set the memory pointer to -1 (i.e. decrementing/calling BETA when the pointer is at 0), the interpreter will raise a runtime error. 

## Hello World
The following code prints "Hello World!" in Brainrot. It was translated from a Brainfuck code sample found on [Wikipedia](https://en.wikipedia.org/wiki/Brainfuck#Hello_World!) with comments removed.
```
SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA
SUS
    SKIBIDI SIGMA SIGMA SIGMA SIGMA
    SUS
        SKIBIDI SIGMA SIGMA
        SKIBIDI SIGMA SIGMA SIGMA
        SKIBIDI SIGMA SIGMA SIGMA
        SKIBIDI SIGMA
        TOILET TOILET TOILET TOILET BETA
    AMOGUS
    SKIBIDI SIGMA
    SKIBIDI SIGMA
    SKIBIDI BETA
    SKIBIDI SKIBIDI SIGMA
    SUS TOILET AMOGUS
    TOILET BETA
AMOGUS

SKIBIDI SKIBIDI GOON
SKIBIDI BETA BETA BETA GOON
SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA GOON GOON SIGMA SIGMA SIGMA GOON
SKIBIDI SKIBIDI GOON
TOILET BETA GOON
TOILET GOON
SIGMA SIGMA SIGMA GOON BETA BETA BETA BETA BETA BETA GOON BETA BETA BETA BETA BETA BETA BETA BETA GOON
SKIBIDI SKIBIDI SIGMA GOON
SKIBIDI SIGMA SIGMA GOON
```

Of course, you can choose to place everything on one line:
```
SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA SUS SKIBIDI SIGMA SIGMA SIGMA SIGMA SUS SKIBIDI SIGMA SIGMA SKIBIDI SIGMA SIGMA SIGMA SKIBIDI SIGMA SIGMA SIGMA SKIBIDI SIGMA TOILET TOILET TOILET TOILET BETA AMOGUS SKIBIDI SIGMA SKIBIDI SIGMA SKIBIDI BETA SKIBIDI SKIBIDI SIGMA SUS TOILET AMOGUS TOILET BETA AMOGUS SKIBIDI SKIBIDI GOON SKIBIDI BETA BETA BETA GOON SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA SIGMA GOON GOON SIGMA SIGMA SIGMA GOON SKIBIDI SKIBIDI GOON TOILET BETA GOON TOILET GOON SIGMA SIGMA SIGMA GOON BETA BETA BETA BETA BETA BETA GOON BETA BETA BETA BETA BETA BETA BETA BETA GOON SKIBIDI SKIBIDI SIGMA GOON SKIBIDI SIGMA SIGMA GOON
```

## The Other Brainrot

Apparently, there's [another](https://github.com/glapa-grossklag/brainrot) Brainrot programming language by [Miles Glapa-Grossklag](https://github.com/glapa-grossklag). This Brainrot language has nothing to do with that project. Nonetheless, I trust that my sus imposter language will be more sigma and have more rizz than the original.
