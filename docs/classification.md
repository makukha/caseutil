# Cases classification

The two properties bellow let us classify all widely used cases: *word separator* (underscore, hyphen, space, letter case change), and *word case rule*:

## Table

| Words case rule             | Underscore    | Hyphen       | Space           | Case change   |
|-----------------------------|---------------|--------------|-----------------|---------------|
| All `lower`                 | `snake_case`  | `kebab-case` | `lower case`    | ∅<sup>2</sup> |
| 1st `lower`<br>rest `Title` | —<sup>1</sup> | —            | —               | `camelCase`   |
| All `Title`                 | `Ada_Case`    | `Train-Case` | `Title Case`    | `PascalCase`  |
| 1st `Title`<br>rest `lower` | —             | —            | `Sentence case` | ∅             |
| All `UPPER`                 | `CONST_CASE`  | `COBOL-CASE` | `UPPER CASE`    | ∅             |

<sup>1</sup> not widely used, <sup>2</sup> not possible

## Ambiguity

It is easy to observe that when there is a single word (no separators possible), all 12 cases are reduced to 3 classes where cases match to each other:

* `lower`, `camel`, `snake`, `kebab`
* `Title`, `Pascal`, `Ada`, `Train`, `Sentence`
* `UPPER`, `CONST`, `COBOL`

This makes case detection multivalued when there is more than one word.
