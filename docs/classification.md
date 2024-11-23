# Cases classification

The two properties bellow let us classify all widely used cases: *word separator* (underscore, hyphen, space, letter case change), and *word case rule*:

## Table

| Words case rule          | Underscore    | Hyphen       | Space           | Case change   |
|--------------------------|---------------|--------------|-----------------|---------------|
| all words are `lower`    | `snake_case`  | `kebab-case` | `lower case`    | ∅<sup>2</sup> |
| 1st `lower` rest `Title` | —<sup>1</sup> | —            | —               | `camelCase`   |
| all words are `Title`    | `Ada_Case`    | `Train-Case` | `Title Case`    | `PascalCase`  |
| 1st `Title` rest `lower` | —             | —            | `Sentence case` | ∅             |
| all words are `UPPER`    | `CONST_CASE`  | `COBOL-CASE` | `UPPER CASE`    | ∅             |

<sup>1</sup> not widely used, <sup>2</sup> not possible

## Ambiguity

It is easy to observe that when there is a single word (no separators possible), all 12 cases are reduced to 3 classes:

* `lower` = `camel` = `kebab` = `snake`
* `Title` = `Ada` = `Pascal` = `Sentence` = `Train`
* `UPPER` = `COBOL` = `CONST`

This makes case detection multivalued when there is more than one word.
