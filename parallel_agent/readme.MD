# Parallel Agent - Social Media Post Generator

A sophisticated multi-platform social media content generation system built using Google's ADK framework. This project demonstrates parallel agent orchestration combined with sequential processing for creating and analyzing social media content across multiple platforms.

## Overview

The Parallel Agent application generates platform-optimized social media content for Facebook, Instagram, and WhatsApp, then analyzes and synthesizes all outputs into a comprehensive evaluation report.

### Key Features

- **Parallel Processing**: Generate content for multiple platforms simultaneously using `ParallelAgent`
- **Sequential Pipeline**: Chain agents together for structured workflow using `SequentialAgent`
- **Platform-Specific Expertise**: Dedicated agents for each social media platform with specialized instructions
- **Content Analysis**: AI-powered analysis and synthesis of generated content across all platforms
- **LLM Integration**: Powered by Google's Gemini 2.5 Flash Lite model
- **Tool-Based Architecture**: Structured tools for consistent output formatting

## Architecture

### Agent Hierarchy

```
root_agent (SequentialAgent)
├── post_generator (ParallelAgent)
│   ├── facebook_agent (LlmAgent)
│   ├── instagram_agent (LlmAgent)
│   └── whatsapp_agent (LlmAgent)
└── post_analysis_agent (LlmAgent)
```

### Execution Flow

1. **Parallel Generation Phase**
   - All three platform agents (`facebook`, `instagram`, `whatsapp`) execute in parallel
   - Each agent generates platform-optimized content based on the same input topic
   - Results are collected and merged

2. **Sequential Analysis Phase**
   - Output from parallel agents feeds into the analysis agent
   - Comprehensive evaluation of all generated content
   - Cross-platform consistency check and recommendations

## Components

### 1. Social Media Post Agent (Root Agent)

**File**: `social_media_post_agent/agent.py`

The root agent orchestrates the entire workflow:
- Combines parallel post generation with sequential analysis
- Manages data flow between stages
- Exports the final `root_agent` for application use

```python
from social_media_post_agent import root_agent
# root_agent handles the complete pipeline
```

### 2. Parallel Agent - Post Generator

Creates content for multiple platforms simultaneously.

#### Facebook Agent
**Location**: `social_media_post_agent/subagent/facebook_agent/`

- **Model**: Gemini 2.5 Flash Lite
- **Specialization**: Long-form content with engagement focus
- **Key Responsibilities**:
  - Generate engaging Facebook posts
  - Create long-form social media content
  - Optimize engagement and readability
  - Include CTAs when relevant
  - Maintain brand tone consistency

**Tool**: `generate_facebook_post(topic, tone, include_call_to_action)`
- Input: Topic, tone (default: "professional"), CTA flag
- Output: Structured response with post content, platform info, and statistics

#### Instagram Agent
**Location**: `social_media_post_agent/subagent/insatgram_agent/`

- **Model**: Gemini 2.5 Flash Lite
- **Specialization**: Viral content with hashtag strategies
- **Key Responsibilities**:
  - Generate viral captions
  - Create hashtag strategies
  - Optimize engagement
  - Create trendy content
  - Improve discoverability

**Tool**: `generate_instagram_post(topic, tone, include_hashtags)`
- Input: Topic, tone (default: "engaging"), hashtag flag
- Output: Caption, hashtags, post type, and engagement metrics

**Tone Options**: engaging, professional, funny, luxury, casual

#### WhatsApp Agent
**Location**: `social_media_post_agent/subagent/whatsapp_agent/`

- **Model**: Gemini 2.5 Flash Lite
- **Specialization**: Conversational messaging for campaigns
- **Key Responsibilities**:
  - Generate conversational messages
  - Create broadcast campaigns
  - Improve customer engagement
  - Maintain concise communication
  - Create personalized messaging

**Tool**: `generate_whatsapp_campaign_message(topic, tone, include_emoji)`
- Input: Topic, tone (default: "friendly"), emoji flag
- Output: Campaign message, message type, and content metrics

### 3. Sequential Agent - Post Analysis

**Location**: `social_media_post_agent/subagent/post_analyser/`

Analyzes and synthesizes all generated content into actionable insights.

- **Model**: Gemini 2.5 Flash Lite
- **Input**: Facebook post, Instagram caption, WhatsApp message
- **Analysis Coverage**:
  1. **Executive Summary**: Overall campaign quality and brand consistency
  2. **Platform-Specific Analysis**: Evaluate effectiveness for each platform
  3. **Content Evaluation Metrics**:
     - Readability score
     - Emotional engagement
     - CTA effectiveness
     - Audience targeting quality
     - Marketing strength
     - Conversion potential
  4. **Improvement Recommendations**:
     - Hashtag suggestions
     - Better CTA options
     - Content length optimization
     - Emotional trigger improvements
     - Engagement hook enhancements
  5. **Final Campaign Score** (out of 10):
     - Engagement
     - Clarity
     - Conversion potential
     - Virality
     - Brand alignment

## Project Structure

```
parallel_agent/
├── README.md                          # This file
├── social_media_post_agent/
│   ├── __init__.py                   # Exports root_agent
│   ├── agent.py                      # Root agent definition
│   └── subagent/
│       ├── facebook_agent/
│       │   ├── __init__.py
│       │   ├── agent.py              # Facebook agent definition
│       │   └── tool.py               # Facebook content generation tool
│       ├── insatgram_agent/
│       │   ├── __init__.py
│       │   ├── agent.py              # Instagram agent definition
│       │   └── tool.py               # Instagram content generation tool
│       ├── whatsapp_agent/
│       │   ├── __init__.py
│       │   ├── agent.py              # WhatsApp agent definition
│       │   └── tool.py               # WhatsApp content generation tool
│       └── post_analyser/
│           ├── __init__.py
│           └── agent.py              # Analysis agent definition
```

## Usage

### Basic Import and Usage

```python
from parallel_agent import root_agent

# Execute the complete pipeline with a topic
result = root_agent.execute({
    "topic": "AI-powered automation solutions",
    "tone": "professional",
    "include_call_to_action": True
})

# Result contains:
# - facebook_post: Long-form content
# - instagram_caption: Viral caption with hashtags
# - whatsapp_message: Concise campaign message
# - analysis: Comprehensive content analysis and scores
```

### Individual Agent Usage

```python
from social_media_post_agent.subagent.facebook_agent import facebook_agent
from social_media_post_agent.subagent.insatgram_agent import instagram_agent
from social_media_post_agent.subagent.whatsapp_agent import whatsapp_agent

# Generate content for a specific platform
facebook_result = facebook_agent.execute({
    "topic": "New product launch"
})

instagram_result = instagram_agent.execute({
    "topic": "New product launch",
    "tone": "engaging"
})

whatsapp_result = whatsapp_agent.execute({
    "topic": "New product launch",
    "tone": "friendly"
})
```

## Technology Stack

- **Framework**: Google ADK (Agent Development Kit)
- **Language Models**: 
  - Primary: Gemini 2.5 Flash Lite
  - Alternative: Groq (LiteLlm support available)
- **Language**: Python 3.x
- **Agent Types**: `ParallelAgent`, `SequentialAgent`, `LlmAgent`

## Output Format

All agents return structured responses with:

```python
{
    "result": {
        # Agent-specific results
        "platform": "facebook|instagram|whatsapp",
        "post|caption|message": "...",
        # ... platform-specific fields
    },
    "stats": {
        "success": True,
        "post_length": 123,
        # ... metrics
    },
    "additional_info": {
        "tone": "...",
        "generated_at": timestamp,
        "tool_name": "..."
    }
}
```

## Benefits of This Architecture

### Parallelization
- **Performance**: All three platform agents run simultaneously, reducing total execution time
- **Scalability**: Easy to add more platform agents without sequential overhead
- **Efficiency**: Optimal resource utilization

### Sequential Pipeline
- **Validation**: Analysis phase ensures quality across all platforms
- **Consistency**: Cross-platform review before final output
- **Insights**: Comprehensive recommendations based on all platforms

### Specialization
- **Domain Expertise**: Each agent has focused instructions for its platform
- **Quality**: Platform-specific optimization leads to better content
- **Customization**: Easy to adjust tone and style per platform

## Customization Options

### Agent Instructions
Modify the `instruction` parameter in each agent to change behavior:
- Content tone and style
- Target audience focus
- Feature emphasis
- Call-to-action strategies

### Tools
Enhance or replace tools in `tool.py` files to:
- Generate different content formats
- Add metadata extraction
- Integrate with external APIs
- Implement custom formatting

### Models
Switch between models by changing the `model` parameter:
- Use Gemini for balanced performance
- Use Groq for cost optimization
- Mix models for different agents

## Configuration

### Environment Variables
```bash
# Optional: For Groq integration
GROQ_API_KEY=your_groq_api_key

# Optional: For OpenRouter integration
OPENROUTER_API_KEY=your_openrouter_api_key
```

### Model Selection
Currently configured to use `gemini-2.5-flash-lite`. To switch:

```python
# In agent.py files
GEMINI_MODEL = "your-preferred-model"
```

Alternative models (with LiteLlm):
- `groq/openai/gpt-oss-120b`
- `llama-3.1-8b-instant`
- Any model supported by LiteLlm

## Use Cases

1. **Multi-Platform Marketing Campaigns**
   - Generate coordinated content across platforms
   - Maintain brand consistency
   - Optimize for each platform's audience

2. **Content Analysis and Optimization**
   - Evaluate content quality
   - Get improvement recommendations
   - Score content effectiveness

3. **Rapid Content Prototyping**
   - Create multiple versions in parallel
   - Test different tones and styles
   - Analyze results quickly

4. **Marketing Automation**
   - Automate content generation pipeline
   - Integrate with publishing workflows
   - Scale content production

## Error Handling

All tools include try-catch blocks returning:
```python
{
    "result": {"error": str(e)},
    "stats": {"success": False},
    "additional_info": {"error_type": type(e).__name__}
}
```

## Future Enhancements

- [ ] Add image generation for Instagram posts
- [ ] Implement A/B testing framework
- [ ] Integrate with social media publishing APIs
- [ ] Add sentiment analysis
- [ ] Implement multi-language support
- [ ] Add scheduling capabilities
- [ ] Create feedback loop for continuous improvement
- [ ] Add more social platforms (LinkedIn, TikTok, Twitter)

## Related Projects

- **Basic Agent**: Simple single-agent implementation
- **Lite LLM**: Model integration examples
- **Structured Output Agent**: Output schema validation
- **WhatsApp Agent**: Standalone WhatsApp-specific agent

## Notes

- The Instagram agent directory is named `insatgram_agent` (note the typo)
- All agents use Gemini 2.5 Flash Lite by default
- Parallel execution provides optimal performance for multi-platform scenarios
- Analysis agent provides valuable insights for content optimization
- Tools are designed to be extensible for custom implementations

## License

See LICENSE file in the parent directory.
