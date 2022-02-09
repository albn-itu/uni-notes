

# Lecture 3

## The software process

A structured set of activities

- Software specification
- Software development
- Software validation
- Software evolution

### Software specification

+ The process of establishing
  + What services are required
  + The constraints on the systems operation and development
+ Requirement engineering process
  + Feasibility study (Is it financially and technologically feasable)
  + Requirements and elicitation analysis
    + Creates requirement specfication
    + Requirement validation



### Software development

- The process of converting system specification into an executable system
- Software design
  - Design a software structure based on the specification
- Implementation
  - Translate structure into an executable program
- Design and implementation are closely related, and may be hard to distinguish



### Main design activities

- Architectural design
  - How is the architecture, servers, database, etc.
  - Outputs: System architecture
- Interface design
  - How do the systems talk to each other
  - Outputs: Interface specification
- Component design
  - Outputs: Component specification
- Database design
  - Outputs: Database specification



### Software validation

- Vitrifaction and validation is intended to show that a system conforms to its specification, and fullfils the clients needs
  - Verification: "Are we building the product right" (Unit testing)
  - Validation: "Are we building the right product" (Client requirements)
  - Example: A system that does math, but the client wanted UUID checker. The system is verified, and works. But the validation is wrong.
- Development and component testing
  - Individual components are tested individually
  - Unit testing
- System testing
  - Testing the whole system
- Acceptance testing
  - The client test the system fullfils their needs



### Software evolution and maintenance

Not in the scope of this course, but the course: DevOps, Software evolution and software maintenance



## Development models

- Waterfall
  - Just don't
- SCRUM
- Incremental development
  - Specification, Implementation and Validation at the same time
- Reuse-oriented software engineering
  - Assemble the system from existing components



## Software life cycle from an OO perspective

TODO: Insert pic from slides