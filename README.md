![Banner](https://raw.githubusercontent.com/Vyogami/Vadi/main/assets/banner.png)

---

Vadi is a simple, interpreted and dynamically-typed programming language. It comes with its own tool called a REPL, which lets you try out code quickly.

The interpreter which is the part of Vadi that runs your code, uses a technique named "Recursive Descent Parsing." This technique helps the interpreter understand your high-level code by creating a data-structure called a `parse tree`. Then, the interpreter uses this parse tree to figure out what your code is asking it to do.You can check out the Vadi's [Syntax Grammar](#grammar) in BNF for more information.

## Installation

Use [pip](https://pip.pypa.io/en/stable/) or [pipx](https://github.com/pypa/pipx) to install vadi's REPL.

> [!TIP]
> We recommend using [pipx](https://github.com/pypa/pipx) for installing vadi on a global level.

```bash
pipx install vadi
```

OR

```bash
pip install vadi
```

Now, run the REPL.

```bash
vadi
```

## Grammar

The grammar is written in BNF(Backus Naur Form) notation.

```python

<Interpreter> ::= <binary_expression>
                | <unary_expression>
                | <statement>
                | <expression>
                | <VAR>
                | <FLT>
                | <INT>

<binary_expression> ::= <expression> "+" <expression>
                      | <expression> "-" <expression>
                      | <expression> "*" <expression>
                      | <expression> "/" <expression>
                      | <expression> "=" <expression>

<unary_expression> ::= "+" <expression>
                     | "-" <expression>

<statement> ::= "DECL" <variable> "=" <expression>

<expression> ::= <term> "+" <term>
               | <term> "-" <term>

<term> ::= <factor> "*" <factor>
         | <factor> "/" <factor>

<factor> ::= "INT"
           | "FLT"
           | "(" <expression> ")"
           | <VAR>

```

## Syntax

- Unary operations

  ```python
  +1
  -5
  ```

- Binary operations

  ```python
  56+23
  ```

- Complex arithmetic operations

  ```python
  1*2(4+5(5/6))
  ```

- Variable declarations

  ```javascript
  var int = 89;
  var float = 3.1415;
  var difference = int - 20;
  ```

- Conditionals: if-else

  > TODO: [issue#2](https://github.com/Vyogami/Vadi/issues/2)

- Conditionals: loops

  > TODO: [issue#2](https://github.com/Vyogami/Vadi/issues/2)

### Supported datatypes

- Integer
- Float

## Contributing

Issues and Pull Requests are definitely welcome! Check out [Contributing guidelines](./CONTRIBUTING.md) to get started.
Everyone who interacts with the vadi project via codebase, issue tracker, chat rooms, or otherwise is expected to follow the [Code of Conduct](https://github.com/Vyogami/.github/blob/main/CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE).
