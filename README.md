# E-coupon Distribution Application (EC-APP)

The files uploaded in this repository are the formal verification and proof of concept of the protocol proposed in the paper with the title "Anonymous Location-Based Advertising with Fine-Grained Statistics", anonymously submitted to The 20th International Workshop on Security (IWSEC 2025).


## Proof of Concept

The implementation is done using Python and consists of seven scripts:

- **Issuer.py:** Performing the E-coupon issuer’s operations.
- **Client.py:** Illustrating the process at the client.
- **PS.py:** The Proximity Service (PS) at the shop.
- **Ecoupon.py:** A module for customized functions dedicated to the relevant functions in our
context.
- **DataGen.py:** A script for generating e-coupons data.
- **Stats.py:** For the statistics relevant to the advertisement conversion rate.

The video demonstration of the proof of concept can be found in this [link](https://mega.nz/file/CQUXDSAC#m6b4_zKJACLJ0tmj2qNVPJ42kXrY9Lal_NPYGzgW2KY). 

More detailed description can be found in the file _POC.pdf_ in the Proof of Concept folder.

## Formal verification

Formal verification of the protocol is done by using ProVerif tool. We provide two codes for the model of the protocol:

- **Ecoupon.pv:** Proving the secrecy and authentication.
- **Ecoupon.pv:** Proving observational equivalence.

   
## ProVerif

ProVerif is a state-of-the-art tool for formal verification of symbolic modeling and analysis of security protocols. It uses Dolev-Yao as an adversary model. ProVerif uses the applied pi-calculus as a formal language and translates the protocol into a set of Horn clauses. Then, it tries to conclude if some security property is falsified, i.e., finds an attack.

For more information, [Proverif Manual](https://bblanche.gitlabpages.inria.fr/proverif/manual.pdf) is available online.
