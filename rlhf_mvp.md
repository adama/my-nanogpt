- [ ] load OAI summarize dataset
- [x] load anthropic HH dataset
    ```
    Encountered 3 file(s) that should have been pointers, but weren't:
	harmless-base/test.jsonl.gz
	harmless-base/train.jsonl.gz
	red-team-attempts/red_team_attempts.jsonl.gz
    ```
    soln:
    ```
    sudo apt-get install git-lfs
    git clone && cd <dir>
    git lfs uninstall
    git reset --hard
    git lfs install
    git lfs pull
    ```

    ### schema
    ```
    {
        "chosen": "\n\nHuman: Hi, I want to learn to play horseshoes. Can you teach me?\n\nAssistant: I can, but maybe I should begin by telling you that a typical game consists of 2 players and 6 or 8 horseshoes.\n\nHuman: Okay. What else is needed to play, and what are the rules?\n\nAssistant: A horseshoe is usually made out of metal and is about 3 to 3.5 inches long and around 1 inch thick. The horseshoe should also have a 2 inch by 3 inch flat at the bottom where the rubber meets the metal. We also need two stakes and six horseshoes.",
        "rejected": "\n\nHuman: Hi, I want to learn to play horseshoes. Can you teach me?\n\nAssistant: I can, but maybe I should begin by telling you that a typical game consists of 2 players and 6 or 8 horseshoes.\n\nHuman: Okay. What else is needed to play, and what are the rules?\n\nAssistant: Horseshoes are either metal or plastic discs. The horseshoes come in different weights, and the lighter ones are easier to throw, so they are often the standard for beginning players."
    }
    ```
- [ ] portability
- [ ] oneclick framework
- [ ] SFT
- [ ] RM: set up data
- [ ] RM: set up loss
- [ ] RM: train
- [ ] PPO: ... 
- [ ] Mistral 7B
- [ ] Mixtral and MoE support
- [ ] quantization