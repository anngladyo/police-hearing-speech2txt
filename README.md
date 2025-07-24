# Police Hearing Speech-to-Text Report Generator

<img width="882" height="738" alt="image" src="https://github.com/user-attachments/assets/d085693c-fcc8-4d0b-8318-1cb5a8f2601c" />

## Overview

This project provides an automated solution for processing police hearing audio and generating structured reports. The system leverages Azure AI services to transform audio recordings into professional, formatted documents that can be easily reviewed and edited by human operators.

## How It Works

The application follows a streamlined process:

1. **Real-time Speech Transcription**: Police hearing audio is processed using Azure Speech Service, which converts spoken words into text and generates a comprehensive transcription in JSON format.

2. **AI-Powered Report Generation**: The transcription JSON file is sent to Azure OpenAI service along with a structured report template. The AI analyzes the transcript content and generates a professional report that matches the predefined template structure while incorporating relevant data from the hearing transcript.

The generated report is automatically converted from Markdown to DOCX format, creating an editable Word document that human reviewers can modify, annotate, and finalize as needed.

## Key Features

- **Real-time audio processing** using Azure Speech Service
- **Intelligent report structuring** powered by Azure OpenAI
- **Template-based formatting** ensures consistent report structure
- **DOCX output** for easy human editing and review
- **Automated workflow** from audio input to formatted document

## Benefits

- Significantly reduces manual transcription time
- Ensures consistent report formatting across all hearings
- Provides accurate, AI-assisted content extraction
- Delivers editable documents ready for human review
- Streamlines the documentation process for police hearings

## Data Privacy Considerations

For organizations with strict data privacy and security requirements, this architecture can be enhanced with additional privacy-focused components:

### On-Premises Processing Options

1. **Containerized Speech Service**: Azure Speech Service can be containerized and deployed on-premises, ensuring that sensitive audio data never leaves the organization's infrastructure while still leveraging Azure's advanced speech recognition capabilities.

2. **Open Source LLM Integration**: The report generation component can be modified to use open source language models (such as Llama, Mistral, or other locally-hosted models) instead of Azure OpenAI, preventing transcript data from being sent to cloud services.

### Enhanced Data Protection

3. **Personal Information Redaction**: An additional privacy layer can be implemented using Azure Language Service to automatically detect and redact personally identifiable information (PII) from transcripts before report generation, ensuring sensitive details are protected throughout the process.

These enhancements allow organizations to maintain complete control over sensitive hearing data while still benefiting from AI-powered automation and structured report generation.

