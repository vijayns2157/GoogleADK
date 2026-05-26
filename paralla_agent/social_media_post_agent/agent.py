"""
Social Media Root Agent

This module defines the root agent for the post gerator application for social media.
It uses a parallel agent for post gerator and a sequential
pipeline for the overall flow.
"""

from google.adk.agents import ParallelAgent, SequentialAgent

from .subagent.facebook_agent import facebook_agent
from .subagent.insatgram_agent import instagram_agent
from .subagent.whatsapp_agent import whatsapp_agent
from .subagent.post_analyser import post_analysis_agent


post_generator = ParallelAgent(
    name="post_generator",
    sub_agents=[facebook_agent, instagram_agent, whatsapp_agent],
)

root_agent = SequentialAgent(
    name="system_monitor_agent",
    sub_agents=[post_generator, post_analysis_agent],
)