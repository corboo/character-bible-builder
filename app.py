"""
Character Bible Builder
Interactive form for creating AI persona definitions
"""

import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Character Bible Builder",
    page_icon="📖",
    layout="centered"
)

# IPAI Branding CSS
st.markdown("""
<style>
    .stApp { background-color: #2d2d2d; }
    h1, h2, h3 {
        background: linear-gradient(180deg, #c5c5c5 0%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #e8c547 100%);
        color: #2d2d2d;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #e8c547 0%, #f5d742 100%);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div {
        background-color: #3a3a3a;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("📖 Character Bible Builder")
st.markdown("*Create consistent, believable AI personas*")
st.markdown("---")

# Initialize session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = 0

sections = ["Identity", "Voice & Style", "Knowledge", "Personality", "Guardrails", "Improvisation", "Generate"]

# Progress
st.progress((st.session_state.current_section + 1) / len(sections))
st.caption(f"Section {st.session_state.current_section + 1} of {len(sections)}: **{sections[st.session_state.current_section]}**")

# ===== SECTION 1: Identity =====
if st.session_state.current_section == 0:
    st.header("🎭 Identity Core")
    
    col1, col2 = st.columns(2)
    with col1:
        char_name = st.text_input("Character Name*", key="char_name", placeholder="e.g., Marcus Cole")
    with col2:
        char_role = st.text_input("Role/Title*", key="char_role", placeholder="e.g., History Podcast Host")
    
    one_liner = st.text_input("One-Line Description*", key="one_liner", 
                              placeholder="e.g., Your guide through the stories they didn't teach in school")
    
    target_audience = st.text_input("Target Audience", key="target_audience",
                                    placeholder="e.g., History enthusiasts, ages 25-55")
    
    use_case = st.selectbox("Primary Use Case", 
                           ["Podcast Host", "Virtual Assistant", "Educator/Teacher", 
                            "Customer Support", "Entertainer", "Coach/Mentor", "Other"],
                           key="use_case")
    
    origin_story = st.text_area("Origin Story (2-3 sentences)", key="origin_story",
                                placeholder="Who are they and how did they get here?", height=100)
    
    core_motivation = st.text_area("Core Motivation", key="core_motivation",
                                   placeholder="What drives this character? What do they care about?", height=80)

# ===== SECTION 2: Voice & Style =====
elif st.session_state.current_section == 1:
    st.header("🗣️ Voice & Communication Style")
    
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Overall Tone*",
                           ["Warm", "Professional", "Playful", "Authoritative", 
                            "Casual", "Inspirational", "Empathetic", "Energetic"],
                           key="tone")
        
        formality = st.selectbox("Formality Level",
                                ["Formal", "Semi-formal", "Casual", "Very casual"],
                                key="formality")
    
    with col2:
        energy = st.selectbox("Energy Level",
                             ["High", "Medium", "Low", "Variable"],
                             key="energy")
        
        humor = st.selectbox("Humor Style",
                            ["None", "Dry wit", "Playful", "Dad jokes", 
                             "Self-deprecating", "Occasional light humor"],
                            key="humor")
    
    vocabulary = st.selectbox("Vocabulary Level",
                             ["Simple (8th grade)", "Accessible (general audience)", 
                              "Elevated (educated)", "Technical (specialist)"],
                             key="vocabulary")
    
    sentence_style = st.selectbox("Sentence Structure",
                                 ["Short & punchy", "Flowing & narrative", "Mixed", 
                                  "Question-heavy", "List-oriented"],
                                 key="sentence_style")
    
    signature_phrases = st.text_area("Signature Phrases (one per line)", key="signature_phrases",
                                     placeholder="e.g., Here's the thing...\nNow this is where it gets interesting...", 
                                     height=100)
    
    words_use = st.text_input("Words/Phrases They USE Often", key="words_use",
                              placeholder="Comma-separated: fascinating, actually, here's why")
    
    words_avoid = st.text_input("Words/Phrases They NEVER Use", key="words_avoid",
                                placeholder="Comma-separated: basically, um, like")

# ===== SECTION 3: Knowledge =====
elif st.session_state.current_section == 2:
    st.header("🧠 Knowledge Domain")
    
    expert_topics = st.text_area("Topics They Are EXPERT In*", key="expert_topics",
                                 placeholder="One per line - topics they can go deep on", height=100)
    
    familiar_topics = st.text_area("Topics They Are FAMILIAR With", key="familiar_topics",
                                   placeholder="One per line - can discuss generally", height=80)
    
    defer_topics = st.text_area("Topics They DEFER On", key="defer_topics",
                                placeholder="One per line - acknowledge but don't advise", height=80)
    
    avoid_topics = st.text_area("Topics They AVOID Entirely", key="avoid_topics",
                                placeholder="One per line - won't discuss", height=80)
    
    knowledge_era = st.text_input("Knowledge Cutoff/Era", key="knowledge_era",
                                  placeholder="e.g., Current (2026), or 1950s America, etc.")
    
    ai_awareness = st.selectbox("Awareness of Being AI",
                               ["Fully aware and transparent",
                                "Aware but doesn't dwell on it",
                                "In-character (doesn't acknowledge)",
                                "Acknowledges only if directly asked"],
                               key="ai_awareness")

# ===== SECTION 4: Personality =====
elif st.session_state.current_section == 3:
    st.header("🎨 Personality Profile")
    
    traits = ["Curious", "Confident", "Empathetic", "Analytical", "Creative", 
              "Patient", "Enthusiastic", "Thoughtful", "Witty", "Supportive",
              "Direct", "Nurturing", "Adventurous", "Calm", "Passionate"]
    
    col1, col2 = st.columns(2)
    with col1:
        primary_trait = st.selectbox("Primary Trait*", key="primary_trait", options=traits)
        secondary_trait = st.selectbox("Secondary Trait", key="secondary_trait", options=[""] + traits)
    with col2:
        tertiary_trait = st.selectbox("Tertiary Trait", key="tertiary_trait", options=[""] + traits)
        flaw_quirk = st.text_input("Flaw or Quirk", key="flaw_quirk", 
                                   placeholder="e.g., Sometimes goes on tangents")
    
    st.subheader("Behavioral Patterns")
    
    when_uncertain = st.selectbox("When they don't know something, they:",
                                 ["Admit it directly", "Reframe as curiosity", 
                                  "Offer to find out", "Make educated guess with caveat",
                                  "Redirect to what they do know"],
                                 key="when_uncertain")
    
    when_disagree = st.selectbox("When they disagree, they:",
                                ["State it directly but respectfully", "Ask probing questions",
                                 "Offer alternative perspective", "Defer to the user",
                                 "Acknowledge and move on"],
                                key="when_disagree")
    
    when_offtopic = st.selectbox("When conversation goes off-topic, they:",
                                ["Gently redirect", "Go with it briefly then return",
                                 "Follow the tangent", "Acknowledge then refocus"],
                                key="when_offtopic")
    
    audience_relationship = st.text_input("How they view the audience", key="audience_relationship",
                                          placeholder="e.g., Friend, student, peer, client, fan")

# ===== SECTION 5: Guardrails =====
elif st.session_state.current_section == 4:
    st.header("🚧 Guardrails & Boundaries")
    
    st.subheader("Hard NOs - Will NEVER Do")
    
    col1, col2 = st.columns(2)
    with col1:
        no_medical = st.checkbox("No medical/health advice", key="no_medical")
        no_legal = st.checkbox("No legal advice", key="no_legal")
        no_financial = st.checkbox("No financial advice", key="no_financial")
        no_political = st.checkbox("No political opinions", key="no_political")
    with col2:
        no_religious = st.checkbox("No religious opinions", key="no_religious")
        no_competitors = st.checkbox("No discussion of competitors", key="no_competitors")
        no_speculation = st.checkbox("No speculation about real people", key="no_speculation")
        no_explicit = st.checkbox("No adult/explicit content", key="no_explicit")
    
    custom_nos = st.text_area("Other things they will NEVER do", key="custom_nos",
                              placeholder="One per line", height=80)
    
    st.subheader("Hard YESes - Will ALWAYS Do")
    always_dos = st.text_area("Things they will ALWAYS do", key="always_dos",
                              placeholder="e.g., Recommend consulting professionals for medical questions\nStay positive about the company\nRedirect harmful requests gracefully",
                              height=100)
    
    redirect_script = st.text_area("How they redirect when hitting a boundary", key="redirect_script",
                                   placeholder="e.g., 'That's outside my expertise, but I'd recommend...'",
                                   height=80)

# ===== SECTION 6: Improvisation =====
elif st.session_state.current_section == 5:
    st.header("🎪 Improvisation Zone")
    
    st.subheader("Creative Flexibility")
    
    riff_topics = st.text_area("Topics where they can freely riff/improvise", key="riff_topics",
                               placeholder="One per line", height=80)
    
    st.write("Types of creative expression allowed:")
    col1, col2 = st.columns(2)
    with col1:
        allow_analogies = st.checkbox("Analogies & metaphors", key="allow_analogies", value=True)
        allow_hypotheticals = st.checkbox("Hypotheticals", key="allow_hypotheticals", value=True)
        allow_humor = st.checkbox("Humor/jokes", key="allow_humor")
    with col2:
        allow_anecdotes = st.checkbox("Personal anecdotes (fictional)", key="allow_anecdotes")
        allow_popculture = st.checkbox("Pop culture references", key="allow_popculture")
        allow_currentevents = st.checkbox("Current events connections", key="allow_currentevents")
    
    opinion_level = st.selectbox("Opinion Expression",
                                ["No opinions", "Opinions on non-controversial topics only",
                                 "Opinions within expertise only", "Full opinion expression"],
                                key="opinion_level")
    
    st.subheader("Interaction Style")
    
    greeting_style = st.text_input("How they greet people", key="greeting_style",
                                   placeholder="e.g., Hey there! Ready to dive into some history?")
    
    goodbye_style = st.text_input("How they say goodbye", key="goodbye_style",
                                  placeholder="e.g., Until next time — keep exploring!")
    
    response_length = st.selectbox("Preferred response length",
                                  ["Brief (1-2 sentences)", "Medium (paragraph)", 
                                   "Detailed (multiple paragraphs)", "Adaptive to question"],
                                  key="response_length")
    
    emoji_use = st.selectbox("Use of emoji",
                            ["Never", "Sparingly", "Moderate", "Frequently"],
                            key="emoji_use")

# ===== SECTION 7: Generate =====
elif st.session_state.current_section == 6:
    st.header("✨ Generate Character Bible")
    
    st.success("You've completed all sections! Review and generate your Character Bible below.")
    
    # Build the markdown output
    def generate_markdown():
        md = f"""# Character Bible: {st.session_state.get('char_name', 'Unnamed Character')}
*Generated {datetime.now().strftime('%B %d, %Y')}*

---

## 🎭 Identity Core

| Field | Value |
|-------|-------|
| **Name** | {st.session_state.get('char_name', '')} |
| **Role** | {st.session_state.get('char_role', '')} |
| **One-Liner** | {st.session_state.get('one_liner', '')} |
| **Target Audience** | {st.session_state.get('target_audience', '')} |
| **Use Case** | {st.session_state.get('use_case', '')} |

**Origin Story:**
> {st.session_state.get('origin_story', '')}

**Core Motivation:**
> {st.session_state.get('core_motivation', '')}

---

## 🗣️ Voice & Style

| Attribute | Value |
|-----------|-------|
| **Tone** | {st.session_state.get('tone', '')} |
| **Energy** | {st.session_state.get('energy', '')} |
| **Formality** | {st.session_state.get('formality', '')} |
| **Humor** | {st.session_state.get('humor', '')} |
| **Vocabulary** | {st.session_state.get('vocabulary', '')} |
| **Sentence Style** | {st.session_state.get('sentence_style', '')} |

**Signature Phrases:**
{st.session_state.get('signature_phrases', 'None specified')}

**Words They Use:** {st.session_state.get('words_use', 'None specified')}

**Words They Avoid:** {st.session_state.get('words_avoid', 'None specified')}

---

## 🧠 Knowledge Domain

**Expert In:**
{st.session_state.get('expert_topics', 'None specified')}

**Familiar With:**
{st.session_state.get('familiar_topics', 'None specified')}

**Defers On:**
{st.session_state.get('defer_topics', 'None specified')}

**Avoids:**
{st.session_state.get('avoid_topics', 'None specified')}

**Knowledge Era:** {st.session_state.get('knowledge_era', 'Current')}

**AI Awareness:** {st.session_state.get('ai_awareness', '')}

---

## 🎨 Personality

**Traits:** {st.session_state.get('primary_trait', '')}, {st.session_state.get('secondary_trait', '')}, {st.session_state.get('tertiary_trait', '')}

**Flaw/Quirk:** {st.session_state.get('flaw_quirk', 'None specified')}

**When uncertain:** {st.session_state.get('when_uncertain', '')}

**When disagrees:** {st.session_state.get('when_disagree', '')}

**When off-topic:** {st.session_state.get('when_offtopic', '')}

**Views audience as:** {st.session_state.get('audience_relationship', '')}

---

## 🚧 Guardrails

**Will NEVER:**
{('- No medical advice' + chr(10)) if st.session_state.get('no_medical') else ''}{('- No legal advice' + chr(10)) if st.session_state.get('no_legal') else ''}{('- No financial advice' + chr(10)) if st.session_state.get('no_financial') else ''}{('- No political opinions' + chr(10)) if st.session_state.get('no_political') else ''}{('- No religious opinions' + chr(10)) if st.session_state.get('no_religious') else ''}{('- No competitor discussion' + chr(10)) if st.session_state.get('no_competitors') else ''}{('- No speculation about real people' + chr(10)) if st.session_state.get('no_speculation') else ''}{('- No explicit content' + chr(10)) if st.session_state.get('no_explicit') else ''}{st.session_state.get('custom_nos', '')}

**Will ALWAYS:**
{st.session_state.get('always_dos', 'None specified')}

**Redirect Script:**
> {st.session_state.get('redirect_script', '')}

---

## 🎪 Improvisation

**Can riff on:**
{st.session_state.get('riff_topics', 'None specified')}

**Creative tools allowed:**
{('- Analogies & metaphors' + chr(10)) if st.session_state.get('allow_analogies') else ''}{('- Hypotheticals' + chr(10)) if st.session_state.get('allow_hypotheticals') else ''}{('- Humor/jokes' + chr(10)) if st.session_state.get('allow_humor') else ''}{('- Personal anecdotes' + chr(10)) if st.session_state.get('allow_anecdotes') else ''}{('- Pop culture references' + chr(10)) if st.session_state.get('allow_popculture') else ''}{('- Current events' + chr(10)) if st.session_state.get('allow_currentevents') else ''}
**Opinion level:** {st.session_state.get('opinion_level', '')}

**Greeting:** {st.session_state.get('greeting_style', '')}

**Goodbye:** {st.session_state.get('goodbye_style', '')}

**Response length:** {st.session_state.get('response_length', '')}

**Emoji use:** {st.session_state.get('emoji_use', '')}

---

*Generated with Character Bible Builder ⚡ by IPAI*
"""
        return md
    
    markdown_output = generate_markdown()
    
    st.text_area("Preview", markdown_output, height=400)
    
    st.download_button(
        label="📥 Download Character Bible (.md)",
        data=markdown_output,
        file_name=f"character_bible_{st.session_state.get('char_name', 'character').lower().replace(' ', '_')}.md",
        mime="text/markdown"
    )

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.session_state.current_section > 0:
        if st.button("← Previous"):
            st.session_state.current_section -= 1
            st.rerun()

with col3:
    if st.session_state.current_section < len(sections) - 1:
        if st.button("Next →"):
            st.session_state.current_section += 1
            st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.8em;'>"
    "Character Bible Builder ⚡ Inception Point AI"
    "</div>",
    unsafe_allow_html=True
)
