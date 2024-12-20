# Cases classification

The two properties bellow let us classify all widely used cases: *word separator* (underscore, hyphen, space, letter case change), and *word case rule*:

```mermaid
block-beta
columns 6
  W["Word case"]:2
  D["Delimiter"]:4
  
  FW["First word"] RW["Other words"]
  UD["underscore"] HD["hyphen"] SD["space"] CD["case change"]
  
  FW1["lower"] RW1["lower"]
  snake(["snake_case"]) kebab(["kebab-case"]) lower(["lower case"]) llc("∅")
  
  FW2["lower"] RW2["Title"]
  ltu("—") lth("—") lts("—") camel(["camelCase"])
  
  FW3["Title"] RW3["Title"]
  ada(["Ada_Case"]) train(["Train-Case"]) title(["Title Case"]) pascal(["PascalCase"])
  
  FW4["Title"] RW4["lower"]
  tlu("—") tlh("—") sentence(["Sentence case"]) tlc("∅")
  
  FW5["UPPER"] RW5["UPPER"]
  const(["CONST_CASE"]) cobol(["COBOL-CASE"]) upper(["UPPER CASE"]) uuc("∅")
  
  classDef Head1 fill:#006400,fill-opacity:0.9,color:white,stroke:white,stroke-width:1px;
  classDef Head2 fill:#228B22,fill-opacity:0.9,color:white,stroke:white,stroke-width:1px;
  classDef Empty fill-opacity:0,stroke-width:0px;
  
  classDef CaseL padding-left:8px,padding-right:8px,fill:#FFB6C1,fill-opacity:0.2,stroke-width:0px,font-weight:bold;
  classDef CaseT padding-left:8px,padding-right:8px,fill:#00BFFF,fill-opacity:0.2,stroke-width:0px,font-weight:bold;
  classDef CaseU padding-left:8px,padding-right:8px,fill:#00FFFF,fill-opacity:0.2,stroke-width:0px,font-weight:bold;
  
  class W,FW,RW,D Head1
  class FW1,RW1,FW2,RW2,FW3,RW3,FW4,RW4,FW5,RW5,UD,HD,SD,CD Head2
  class snake,kebab,lower,camel CaseL
  class ada,train,title,pascal,sentence CaseT
  class const,cobol,upper CaseU
  class llc,ltu,lth,lts,tlu,tlh,tlc,uuc Empty
```

* `—` not widely used
* `∅` not possible

## Ambiguity

1. When there is a single word (no separators possible), all 12 cases reduce to 3 classes:
   * `lower` = `camel` = `kebab` = `snake`
   * `Title` = `Ada` = `Pascal` = `Sentence` = `Train`
   * `UPPER` = `COBOL` = `CONST`

2. When there is a single character (Title and UPPER match), all 12 cases reduce to 2 classes:
   * `lower` = `camel` = `kebab` = `snake`
   * `Title` = `Ada` = `Pascal` = `Sentence` = `Train` = `UPPER` = `COBOL` = `CONST`

This makes case detection multivalued when there is a single word or single character.
