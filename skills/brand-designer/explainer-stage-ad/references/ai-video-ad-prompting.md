# AI video ad prompting

The craft spine shared by every AI video ad skill in this pack. Those skills come in two kinds and
this file sits under both.

- A **style skill** owns what the ad is made of: the palette, the materials, the named sub-styles.
  `claymation-ad` and `paper-animation-ad` are style skills.
- A **format skill** owns what drives the ad: a song, a character talking, and the structure that
  follows from it. `song-ad` and `talking-character-ad` are format skills.

The two compose. A format skill decides the ad is a character talking to camera; a style skill
decides that character is made of clay. Where both are in play, the style skill's locked block is
what goes in the front of every prompt, and the format skill owns the beat plan.

This file owns what stays the same either way. Read it once, then apply it to every image prompt
and every video prompt you write.

## 1. The style block goes first, and goes in verbatim

A style skill defines one or more **style blocks**: a fixed paragraph describing the medium, the
light, the surface and the imperfection. Where no style skill is in play, write one anyway, in the
same shape, and lock it. That block is the first thing in the prompt, before the subject, before
the action, before the camera.

Two rules, both load bearing:

- **First position.** Image and video models weight the opening of a prompt more heavily than the
  tail. A style described after the action gets applied to the action loosely, if at all.
- **Verbatim.** Copy the block character for character. Do not paraphrase it, do not compress it,
  do not improve the wording between shots. The block is what holds ten shots in one world. Every
  rewrite is a small drift, and by shot six the ad no longer looks like one piece.

A prompt is therefore: style block, then subject, then one action, then camera, then any negative.

## 2. Everything in the frame is made of the same stuff

The most common failure in a stylised ad is one real element sitting inside a stylised world. A
photographic phone screen in a clay scene. A real coffee splash in a paper scene. A crisp vector
logo on a hand-built set.

State the material for every element you name, including the ones that would not normally have a
material:

- text and logos: sculpted, cut, folded or painted in the medium
- liquid, smoke, steam, fire
- screens and UI: rendered as a physical surface in the medium, not a composited screenshot
- shadows and reflections: cast by real light on a real surface

If an element cannot be made in the medium, cut it from the shot rather than letting the model
guess.

## 3. Name the behaviour of the material, not an adjective for it

Handmade and tactile are adjectives. A model cannot render an adjective. It can render a behaviour.

Write what the material does under light, under pressure, and at an edge:

- how the edge reads: soft and rounded, sharp and cut, torn and fibrous
- how the light sits: absorbed and matte, scattered through, bounced off
- where the maker's hand shows: fingerprints, tool marks, fold creases, a seam that did not close
- how it sags, bends, holds or springs back

The imperfection is not decoration. It is the thing that separates the style from a plastic render
of the style, and models default to the clean plastic version unless you ask otherwise by name.

## 4. The camera is a real camera in a small real room

Describe the shot as if a camera operator were standing in the set holding a physical lens.

Do this: macro lens, 12 inches from the subject, slight downward angle, shallow focus falling off
behind the label.

Not this: cinematic 3D render, camera flies through the scene, epic dolly, unreal engine. Render
vocabulary pushes the output toward game-engine CGI and away from the built world, and a camera
move that no real rig could make is the fastest way to break the illusion the style block bought
you.

Name the lens, the distance, the height and the one move. That is enough.

## 5. One subject action per shot, stacked with up to three layers of motion

A video prompt gets exactly one **subject action**. The subject does one thing.

That is not the same as a frame with one moving part. A shot worth watching stacks up to three
layers of motion at once, and only the first of them is capped at one:

- **the subject** does one thing: turns, reaches, opens, falls, sings a line
- **the camera** may add one move: a push-in, a slow orbit, a tilt, a whip
- **the environment** may react: particles lift, light shifts, a wall responds, a shadow swings

Two subject actions in one prompt is where clips go wrong: the model splits its attention, morphs
the subject halfway through, or does one of the two and ignores the other. A six second ad is three
or four shots with one subject action each, not one shot trying to carry four.

A shot carrying only one of the three layers is dead air, and a character standing still while it
talks is the most common case of it. Stack at least two.

**Verify a subject action by measuring where it happens, not across the whole frame.** Comparing
consecutive frames is the right check, but a whole-frame average under-detects a small change: four
bars growing on one desk moved 34 units inside their own region and only 13 across the full frame,
and a one-second sample in the middle of the clip read as almost nothing at all. So sample the whole
clip rather than a window, crop to the region the action occupies, and only then decide it failed.
A clip called dead on a whole-frame average is the easiest good clip to throw away.

**The camera competes with the subject, so decide which one the shot is about.** A prompt carrying
both a subject action and a camera move can come back with only the camera move performed, because
a push-in is easier to render than an object rearranging itself. Verified twice: a figure asked to
turn and lower its arm did only the turn, and a stack of cards asked to slide apart while the camera
pushed in did only the push-in. Where the subject action IS the point of the shot, hold the camera
still and let the subject carry it. Confirmed on the third try: the same kind of shot with the camera
explicitly locked off, and camera movement named in the negative prompt, performed its subject action
cleanly.

Where an ad needs a sequence of actions, that is a shot list, not a longer prompt.

## 6. Timing and frame rate are part of the look

Handmade styles carry an expectation about how motion is sampled. Stop-motion reads at a stepped,
lower effective frame rate, with held poses and a small jitter between frames. Smooth interpolated
motion at full frame rate reads as CGI wearing a costume.

If the style calls for stepped motion, ask for it explicitly in the video prompt, in the words the
style skill gives you. Models default to smooth.

**The line works, the number does not.** Asking for stepped motion reliably produces stepped
motion. Asking for a specific rate does not set the rate. Two clips from the same model with the
same "roughly 12 frames per second" wording came back stepping at different cadences, one holding
each frame for two of a 24fps file (12fps) and one holding for three (8fps). So ask for the
stepping, then measure what you got by comparing consecutive frames, and match your other clips to
whichever cadence the first one chose rather than to the number you asked for.

## 7. Transitions are made with frames, not with words

Do not describe a transition inside a prompt. "Then it cuts to" and "it morphs into" both produce
mush, because the model tries to render the transition as an event in the scene.

Use the start and end frame workflow instead:

1. Generate the still that ends shot A. Keep it.
2. Feed that exact still as the **start frame** of shot B.
3. Prompt shot B for its one motion only.

The continuity comes from the shared frame, not from the language. This also makes the join
editable later: a cut, a dissolve or a whip is an edit decision, made in the timeline, after you
have clips that match.

**This does not contradict section 11, and the difference matters.** Section 11 says never derive a
shot from the previous shot's output. Section 7 says feed shot A's end frame into shot B. Those act
on two different things:

- **Identity** comes from the hero plate. Every still is generated from the plate, never from an
  earlier still, because identity errors compound (verified: a beat generated from the previous
  beat's output came back unreadable, and the same beat generated from the plate was clean).
- **Motion continuity** comes from the shared frame. A still you already generated from the plate
  can be handed to a video model as a start frame, and shot A's final rendered frame can start shot
  B's clip.

So: generate every still from the plate, then chain the **clips** through shared frames. Do not
generate a new still from an old clip's frame, which is the move that breaks identity. Where two
beats need to look like one continuous space, build both stills from the plate plus the same set
plate rather than deriving the second from the first, or the set will quietly change between them.

## 8. Reroll before you rewrite

When a generation misses, the instinct is to add words. Usually the prompt was fine and the seed
was not.

Run the same prompt three times before changing a single word. Generation is stochastic, and the
spread between three seeds on one prompt is often wider than the spread between two prompts. Only
after three misses on the same prompt is the prompt the suspect, and then change **one** thing and
run three more. Changing four things at once means learning nothing from the result.

Budget for this. A finished shot is rarely the first render.

**This rule is easy to write and hard to follow.** The temptation under a bad render is to fix the
words, because that feels like progress. Rewriting three times in a row teaches you nothing about
which change helped, and it burns the same credits a reroll would have. Reroll first.

## 8a. A negation in a positive prompt does the opposite

Image and video models do not process "no" in the prompt they are conditioning on. Writing "no
curtains, no podium, no pink" puts curtains, a podium and pink into the conditioning, and you get
more of them, not less.

Verified the hard way: a plate prompt asking for an empty cyan sweep with "no curtains, no podium,
no plinth, no riser, no spotlight" came back with curtains, a three-tier podium and a spotlight.

So:

- **Write the positive prompt purely affirmatively.** Describe what IS in the frame. "One continuous
  curved surface, uniform flat cyan, bare" rather than "a room with nothing in it".
- **Put every exclusion in the model's negative-prompt field**, where it is handled as a real
  negative.
- **Check the model actually has that field.** Several image models do not, and a model that does
  not have it will accept your negative prompt and silently discard it. Where there is no negative
  field, affirmative wording is the only lever you have.

**More generally, do not assume a model takes the field you want.** A field a model does not have
is accepted and dropped without an error, so an explicit instruction can vanish silently. An
explicit 9:16 request went to a model with no aspect-ratio field and returned 4:3, and nothing in
the response said so. Check the model's own schema before trusting that a parameter took effect,
and look at the output rather than at the success message.

## 8b. Silent does not mean silent

A format that lays narration or a song under its visuals needs the visuals to carry no audio of
their own. Asking for a silent clip is not enough: video models return an audio track whether or not
you requested one, and it is not empty. Two clips generated with no audio request came back at
-26 dB and -34 dB of invented room tone, quiet enough to miss on a laptop speaker and loud enough to
muddy a voiceover underneath it.

So strip the audio stream explicitly at assembly on every clip meant to be silent, rather than
trusting that it is. Check it with a level read rather than by listening once.

## 9. Text in the frame

On-screen text in a stylised ad has two jobs that pull against each other: it has to be made of the
medium, and it has to be readable at thumbnail size on a phone with the sound off.

- Keep it to three or four words. Generated lettering degrades fast past that.
- Reserve contrast for it when you choose the palette. A frame of mid-tones has nowhere to put a
  legible word.
- Where the line has to be exact (a price, an offer, a brand name, a legal line), set it in the
  edit as a real type layer over the generated plate. Do not ask the model to spell something that
  has to be right.

## 10. What is still true regardless of the style

A stylised ad is an ad. The style changes how it looks and changes nothing about what it claims.

- **The product depicted is the product sold.** A sculpted, folded or painted version of the
  product must not show a feature, a size, a quantity or an included accessory the real one does
  not have. Stylisation is not a defence, because the claim is what the viewer takes away.
- **Check the brand's own generated-content rules before you cast anything.** Mature brands keep a
  written contract about what a model may and may not draw, and it is the highest-consequence input
  on the whole job. Ask for it by name, along with any do-not-generate list. Three things it
  routinely forbids, all of which are the obvious creative choice if nobody checked:
  - **The brand's mascot.** Asking a model for "the brand's blue mascot" returns a variant of it,
    which is drift, and drift in a mascot is what the brand system exists to stop. A mascot, a logo
    and a wordmark enter generated output by compositing the real file after generation, never by
    being drawn.
  - **A persona the product does not ship yet.** Some brands keep named identities that are built
    but dormant. Putting one in an ad promises something the product cannot do today.
  - **Colours reserved for a meaning.** An accent that signals one thing in the product cannot be
    repainted onto a character for looking nice.
  Where no such contract exists, say so, and treat the live site and packaging as the brand
  evidence instead.
- **No real person's likeness, and no third-party brand, logo or artwork in frame** without
  confirmed rights. A stylised likeness is still a likeness.
- **Synthetic-media disclosure is a question for the user, not a decision you make silently.**
  Platform rules and local law both move. Raise it, name the placement, and let the user rule.
- **Never promise a lift.** Creative style changes how an ad performs in both directions, and which
  way it went is a measurement question, not a prediction.

## 11. Anything that recurs needs one locked reference, re-attached every time

**Every generation is self-contained.** The model remembers nothing between one render and the
next. "The same character as before" and "keep the jar consistent" mean nothing to it, because
there is no before.

So anything that has to stay the same across shots gets a **hero reference**: one clean plate of
that element on its own, neutral pose, plain background, in the chosen style. One for the
character, one for the product, one for a set that has to hold.

Then, in every later generation where that element appears:

- **re-attach** the plate as a reference image, and
- **re-describe** the element in words, in the prompt

Both, not either. The attachment carries the look, the description tells the model what it is
looking at and what matters about it. Skills that do one and not the other drift by the third shot.

**Never chain off the previous shot's output.** Using shot 2's frame as the reference for shot 3
compounds every small error, and by shot six the element has quietly become something else. Every
shot derives from the original plate.

**The set needs a plate too, and this is the one people skip.** A character plate holds the
character and says nothing about the room, so two beats built from the same character plate in "the
same office" come back as two different offices. Generate an **empty set plate** before any beat,
attach it alongside the character plate in every beat that shares that space, and re-describe the
space in words as well. Verified the hard way: an ad whose beat 1 was a cardboard office with four
desks cut to a beat 2 that had become a sparse empty room, because only the character was plated.

**Faces drift before anything else.** Identity survives at the level of "same person" long after the
face stops matching, because a face is small in frame and carries the most detail. Re-describe the
specific features in every prompt, the nose, the eye shape, the mouth, rather than writing "the same
face as the plate". Where the ad allows it, hold the character at a distance where the face is not
carrying the shot.

## 12. Role-label every attached reference

When a generation takes more than one reference image, say in the prompt which attached image is
which, by its number and its job.

Write: "image 1 is the character plate, image 2 is the start frame of this beat, image 3 is the
product". Unlabelled references get blended into an average of themselves, which is how a product
ends up wearing the character's colours.

The same discipline applies to spoken lines. Put the line in quotation marks, name the delivery,
and keep the words plain and easy to pronounce. A model that has to guess at the tone picks a
neutral read, and a model that meets an unusual word mangles it.

## 13. Known limitations of current models

Honest failure modes to plan around rather than discover on the fourth render. These are reported
behaviours of current image and video models, not a benchmark this pack has run, so treat the table
as a starting checklist and update it from what you actually see.

| What breaks | What it looks like | What to do |
|---|---|---|
| Hands and fingers | Extra digits, fused fingers, a hand that changes count between frames | Keep hands out of close focus, or keep them simple shapes in the medium |
| Spelled text | Almost-words, mirrored letters, a different spelling each render | Three or four words maximum, and set exact copy as a type layer in the edit |
| Long clips | Drift: the subject slowly stops being the same object | Short shots, and rebuild continuity with start frames rather than length |
| Two subjects interacting | One absorbs the other, or they swap attributes | One subject per shot wherever the story allows |
| Fine product detail | Labels, logos and small mechanisms get invented | Hold the product at a distance where invented detail is not readable, or composite the real label |
| Fast camera moves | Smearing, geometry that folds through itself | Slow the move, or hold the camera and move the subject |
| A word with a second meaning | "Stage" returns theatre curtains and a raised plinth. "Cove" returns a beach | Name the physical thing: a curved studio backdrop, one continuous surface |
| An empty frame | Models fill space. Asking for "empty" gets you furniture | Describe the one surface that IS there, and put the objects in the negative field |

When a shot keeps failing after three seeds and one change, the answer is usually to redesign the
shot rather than to keep prompting. A shot the model cannot hold is a shot the ad does not need.
