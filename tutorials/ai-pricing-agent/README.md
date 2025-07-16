# AI Pricing Agent

An intelligent AI agent that automatically collects pricing information from various shops using Groq for AI capabilities, browser automation for web scraping, and Mapbox API for location-based functionality.

## Overview

This tutorial demonstrates how to build a comprehensive AI pricing agent that meets enterprise-level requirements for automated price collection and analysis. The agent combines multiple technologies to provide accurate, location-aware pricing data with proper error handling and retry mechanisms.

## Features

✅ **Multi-Item Price Collection**: Accept and validate lists of items for batch processing  
✅ **AI-Powered Parsing**: Use Groq API to intelligently extract and normalize pricing data  
✅ **Location Intelligence**: Integrate Mapbox API for geographic location data  
✅ **Concurrent Processing**: Handle multiple shop sources simultaneously for efficiency  
✅ **Browser Automation**: Navigate and extract data from dynamic websites  
✅ **Robust Error Handling**: Implement retry logic with exponential backoff  
✅ **Structured Output**: Return comprehensive metadata with confidence scores  
✅ **Configurable Sources**: Easily add or modify shop sources  

## Requirements Met

This implementation fulfills all requirements from the specification:

### Requirement 1: Item List Processing
- ✅ Accepts and validates item list format
- ✅ Initiates price collection from multiple sources
- ✅ Returns structured pricing data for each item

### Requirement 2: Groq AI Integration
- ✅ Uses Groq API for intelligent price parsing
- ✅ Handles Groq processing errors gracefully
- ✅ Normalizes data into consistent format

### Requirement 3: Mapbox Location Services
- ✅ Retrieves location data using Mapbox API
- ✅ Associates location with price information
- ✅ Continues operation when Mapbox is unavailable

### Requirement 4: Python Backend Service
- ✅ Implements retry logic with exponential backoff
- ✅ Provides detailed error logging for debugging
- ✅ Returns responses in consistent JSON format
- ✅ Validates API keys and configurations on startup

### Requirement 5: Multiple Shop Sources
- ✅ Queries multiple shop sources concurrently
- ✅ Adapts parsing approach for different formats
- ✅ Reports failed sources while continuing with available ones

### Requirement 6: Browser Automation
- ✅ Uses browser automation for web navigation
- ✅ Handles JavaScript-rendered dynamic content
- ✅ Interacts with page elements for data extraction

### Requirement 7: Comprehensive Metadata
- ✅ Includes shop name, availability, and timestamp
- ✅ Provides geographic coordinates and address information
- ✅ Returns confidence scores for price accuracy

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/HiminaCaleb/groq-api-cookbook.git
   cd groq-api-cookbook/tutorials/ai-pricing-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the tutorial directory:
   ```bash
   # Required
   GROQ_API_KEY=your_groq_api_key_here
   
   # Optional (for location features)
   MAPBOX_API_KEY=your_mapbox_api_key_here
   ```

## Quick Start

### Basic Usage

```python
import asyncio
from pricing_agent import get_pricing_data

async def main():
    items = ["wireless headphones", "gaming laptop", "smartphone"]
    result = await get_pricing_data(items)
    print(f"Found {result['prices_found']} prices!")

asyncio.run(main())
```

### Run the Example

```bash
python example.py
```

## Architecture

The AI Pricing Agent is built with a modular architecture:

```
PricingAgent
├── ConfigManager      # API key validation and configuration
├── RetryHandler       # Exponential backoff retry logic
├── LocationService    # Mapbox API integration
├── GroqProcessor      # AI-powered price extraction
├── WebScraper        # Browser automation for web scraping
└── PriceData         # Structured data models
```

### Core Components

#### ConfigManager
- Validates required API keys on startup
- Manages environment configuration
- Provides graceful degradation for optional services

#### RetryHandler
- Implements exponential backoff for failed operations
- Configurable retry attempts and delays
- Preserves original error context for debugging

#### LocationService
- Integrates with Mapbox Geocoding API
- Provides geographic coordinates and place names
- Handles API failures gracefully with proper logging

#### GroqProcessor
- Uses Groq API for intelligent price extraction
- Normalizes data across different shop formats
- Returns confidence scores for price accuracy

#### WebScraper
- Automates browser interactions for data extraction
- Handles dynamic JavaScript-rendered content
- Simulates real user behavior to avoid detection

## Usage Examples

### 1. Basic Price Collection

```python
from pricing_agent import get_pricing_data

# Simple usage
items = ["laptop", "headphones"]
result = await get_pricing_data(items)
```

### 2. Custom Configuration

```python
from pricing_agent import PricingAgent

# Create agent with custom settings
agent = PricingAgent()

# Validate input
validated_items = agent.validate_items(["item1", "item2", ""])

# Collect prices
result = await agent.collect_pricing_data(validated_items)
```

### 3. Error Handling

```python
try:
    result = await get_pricing_data(["valid_item"])
    print(f"Success: {result['prices_found']} prices found")
except ValueError as e:
    print(f"Input validation error: {e}")
except Exception as e:
    print(f"Processing error: {e}")
```

## API Response Format

```json
{
  "status": "success",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "execution_time_seconds": 4.23,
  "items_requested": 2,
  "prices_found": 6,
  "shop_sources_used": 3,
  "data": [
    {
      "item_name": "wireless headphones",
      "shop_name": "Amazon",
      "price": 29.99,
      "currency": "USD",
      "availability": "in_stock",
      "url": "https://amazon.com/s?k=wireless headphones",
      "timestamp": "2024-01-15T10:30:00.000Z",
      "location": {
        "coordinates": [-122.4194, 37.7749],
        "place_name": "San Francisco, California, United States",
        "confidence": 0.95
      },
      "confidence_score": 0.89
    }
  ]
}
```

## Configuration

### Shop Sources

The agent supports multiple shop sources that can be configured:

```python
shop_sources = [
    ShopSource("Amazon", "https://amazon.com", "/s?k={item}"),
    ShopSource("Best Buy", "https://bestbuy.com", "/site/searchpage.jsp?st={item}"),
    ShopSource("Target", "https://target.com", "/s?searchTerm={item}")
]
```

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Your Groq API key for AI processing |
| `MAPBOX_API_KEY` | No | Mapbox API key for location services |

## Error Handling

The agent implements comprehensive error handling:

- **Input Validation**: Validates item lists and filters invalid entries
- **API Failures**: Retry logic with exponential backoff for API calls
- **Network Issues**: Graceful handling of network timeouts and connection errors
- **Service Degradation**: Continues operation when optional services fail
- **Detailed Logging**: Comprehensive logging for debugging and monitoring

## Performance Features

- **Concurrent Processing**: Processes multiple shops simultaneously
- **Async Operations**: Non-blocking I/O for improved performance
- **Retry Logic**: Automatic retry with backoff for failed operations
- **Caching Ready**: Architecture supports caching implementation
- **Configurable Timeouts**: Adjustable timeouts for different operations

## Extending the Agent

### Adding New Shop Sources

```python
# Add a new shop to the sources list
new_shop = ShopSource(
    name="NewShop",
    base_url="https://newshop.com",
    search_pattern="/search?query={item}"
)
agent.shop_sources.append(new_shop)
```

### Custom Price Extraction

```python
# Override the Groq processor for custom extraction logic
class CustomGroqProcessor(GroqProcessor):
    async def extract_price_info(self, raw_data: str, item_name: str):
        # Custom extraction logic
        return custom_result
```

## Troubleshooting

### Common Issues

1. **Missing API Keys**: Ensure GROQ_API_KEY is set in your environment
2. **Network Timeouts**: Check internet connection and firewall settings
3. **Rate Limiting**: Implement delays between requests if hitting rate limits
4. **Browser Issues**: Ensure proper browser automation dependencies

### Debug Mode

Enable debug logging for detailed troubleshooting:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## License

This tutorial is part of the Groq API Cookbook and follows the same licensing terms.

## Contributing

Contributions are welcome! Please follow the contribution guidelines in the main repository.

## Support

For questions and support:
- 💬 Join the [Groq Discord community](https://discord.com/invite/groq)
- 🐛 Report issues on [GitHub](https://github.com/groq/groq-api-cookbook/issues)
- 📖 Check the [Groq API documentation](https://console.groq.com/docs)