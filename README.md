# edge-learner

A model and utility for learning market inefficiency patterns with minimal help of humans. It has not yet been decided what sort of model to use yet. It's being thought about and discussed on [the related BHW thread](https://www.blackhatworld.com/seo/follow-me-as-i-create-an-ai-trading-bot-for-bitcoin-crypto.1116066/).

## Binary Options Idea

I just remembered an idea I previously had. It would be nice to be able to start small, without riches. That's
difficult because it means you have to place high leveraged trades. Binary options might be a good place to
start instead since starting from a small portfolio is a bit more straight-forward in that situation.

With this in mind, let's see if we can get an unofficial API to PrimeXBT working (There's no official one).

## TODO

*  Settle on a learning model.
*  Create an interactive charting environment to host the human interaction utility.
    - [d3fc](https://d3fc.io/)
    - [techan.js](https://github.com/andredumas/techan.js)
    - Started here: [github.io/edge-learner/ui](https://thedoctorai.github.io/edge-learner/ui)
*  Create a charting utility capable of visually defining market inefficiencies.
*  Create or adopt a DSL for mathematically defining market inefficiencies.
*  Create a reinforcement model trading agent (Separate repo) which can utilize edge-learner.



## Help Support The Project

This project would benefit from some compute servers, software licenses, and occasional code bounties. Help ensure that there's always a free, open-source version maintained.

**Donate Bitcoin:** `bc1q83q4f69u5700sqvn7l7y2cdjwpkhvlq39cdswv`

**Donate Ethereum**: `0x79933F7fCd8B5045C52Ac581F857B7232cEd4Dc3`



## License

Edge-learner will not start with a commercially permissive license this time. If it works out well, it will probably wind up being a dual license situation. For now,  I'm placing a non-commercial license. There just isn't enough time for  me to work on a commercial permissive licensed project right now.  Approved contributors who put forward good work will be considered for  complimentary commercial licenses and other such agreements in the  future.

Edge-learner is licensed under the [Non-Profit Open Software License 3.0 (NPOSL-3.0)](https://github.com/TheDoctorAI/edge-learner/blob/master/LICENSE.md)

