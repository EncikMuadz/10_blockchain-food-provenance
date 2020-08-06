### Overview
- repo: https://github.com/EncikMuadz/10_blockchain-food-provenance
- Trackback Food to its Source
- provenance use case

##### Problem Statement
Some niche want to eat organic. They can buy organic, but is it really organic? If there is an outbreak of bird-flu in few poultry farms, did we know if the chicken leg in your plate came from one of those infected farms?

Using blockchain technology (later integrated with IoT):
    - implement a system that can help consumers trace back the journey of fresh produce or meat to its source.
    - thereby, consumers can buy the product with a lot more trust.

##### Opportunity:
- The application is extendable to other market like: 
  - parents concern about child's milk, source of junk food
  
### Progress
- `Use Case` -> `WIP`
- Choosing tech stack -> `WIP`
  - Language -> `Python`(preferably), `C++`(2nd choice), `Erlang`(3rd Choice), `Golang` (4th Choice)
  - Web -> `Flask`(preferably), `WASM`(2nd choice)
  - IoT -> `None` for initial stage, add later
    - MQTT (Message broker) ->`USING`
    - module -> https://pypi.org/project/paho-mqtt/ -> `TBD`

- environment
  - wsl python env -> `WIP`
  - git bash -> `DONE`

- architecture

- algorithm
  - PoA(Proof of Authority) -> `Chosen`
    - A pre-approved set of authorities using their identity and staking their reputation to process txs
    - higly tolerant to 51% attack
    - simplify validation process and reduce power consumption
    - suitable for supply chain use case

- codebase
  - scaffold(Program loop) -> simple -> `WIP`
  - p2p network -> threads, sockets -> `WIP`

- recipe
  - activate environment -> anaconda or virtualenv
  - run `driver.py`