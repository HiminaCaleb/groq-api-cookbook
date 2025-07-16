"""
Example usage of the AI Pricing Agent

This script demonstrates how to use the pricing agent to collect
pricing information for a list of items from multiple shops.
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from pricing_agent import get_pricing_data, PricingAgent

# Load environment variables
load_dotenv()

async def example_basic_usage():
    """Basic example of using the pricing agent"""
    print("🔍 AI Pricing Agent - Basic Example")
    print("=" * 50)
    
    # List of items to search for
    items = [
        "wireless headphones",
        "gaming laptop", 
        "smartphone"
    ]
    
    print(f"Searching for prices of: {', '.join(items)}")
    print("This may take a moment as we search multiple shops...\n")
    
    try:
        # Get pricing data
        result = await get_pricing_data(items)
        
        # Display results
        print(f"✅ Search completed!")
        print(f"📊 Found {result['prices_found']} prices from {result['shop_sources_used']} shops")
        print(f"⏱️ Execution time: {result['execution_time_seconds']} seconds\n")
        
        # Display price data for each item
        for price_data in result['data']:
            print(f"🛍️ {price_data['item_name']} at {price_data['shop_name']}")
            print(f"   💰 Price: {price_data['currency']} {price_data['price']}")
            print(f"   📦 Availability: {price_data['availability']}")
            print(f"   🎯 Confidence: {price_data['confidence_score']:.2f}")
            if price_data.get('location'):
                print(f"   📍 Location: {price_data['location']['place_name']}")
            print(f"   🔗 URL: {price_data['url']}")
            print()
        
    except Exception as e:
        print(f"❌ Error: {e}")

async def example_custom_configuration():
    """Example showing custom configuration of the pricing agent"""
    print("🔧 AI Pricing Agent - Custom Configuration Example")
    print("=" * 60)
    
    # Create agent instance for custom configuration
    agent = PricingAgent()
    
    # Validate specific items
    items = ["bluetooth speaker", "tablet", ""]  # Note: empty string should be filtered
    
    try:
        validated_items = agent.validate_items(items)
        print(f"✅ Validated items: {validated_items}")
        
        # Collect pricing data
        result = await agent.collect_pricing_data(validated_items)
        
        # Show summary statistics
        print(f"\n📈 Summary Statistics:")
        print(f"   • Items requested: {result['items_requested']}")
        print(f"   • Prices found: {result['prices_found']}")
        print(f"   • Shop sources: {result['shop_sources_used']}")
        print(f"   • Success rate: {(result['prices_found'] / (result['items_requested'] * result['shop_sources_used']) * 100):.1f}%")
        
    except ValueError as e:
        print(f"❌ Validation error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

async def example_error_handling():
    """Example demonstrating error handling"""
    print("🚨 AI Pricing Agent - Error Handling Example")
    print("=" * 50)
    
    # Test with invalid input
    invalid_inputs = [
        [],  # Empty list
        [""],  # List with empty string
        None,  # None value
        "not a list"  # Wrong type
    ]
    
    for i, invalid_input in enumerate(invalid_inputs, 1):
        print(f"\nTest {i}: {invalid_input}")
        try:
            result = await get_pricing_data(invalid_input)
            print(f"   ✅ Unexpected success: {result}")
        except Exception as e:
            print(f"   ❌ Expected error: {e}")

def check_environment():
    """Check if required environment variables are set"""
    print("🔐 Environment Check")
    print("=" * 30)
    
    required_vars = ["GROQ_API_KEY"]
    optional_vars = ["MAPBOX_API_KEY"]
    
    all_good = True
    
    for var in required_vars:
        if os.getenv(var):
            print(f"✅ {var}: Set")
        else:
            print(f"❌ {var}: Missing (Required)")
            all_good = False
    
    for var in optional_vars:
        if os.getenv(var):
            print(f"✅ {var}: Set")
        else:
            print(f"⚠️ {var}: Missing (Optional - location features disabled)")
    
    return all_good

async def main():
    """Main example runner"""
    print("🤖 AI Pricing Agent Examples\n")
    
    # Check environment
    if not check_environment():
        print("\n❌ Please set required environment variables before running examples.")
        print("Create a .env file with:")
        print("GROQ_API_KEY=your_groq_api_key_here")
        print("MAPBOX_API_KEY=your_mapbox_api_key_here  # Optional")
        return
    
    print("\n" + "="*70)
    
    # Run examples
    try:
        await example_basic_usage()
        print("\n" + "="*70)
        
        await example_custom_configuration()
        print("\n" + "="*70)
        
        await example_error_handling()
        
    except KeyboardInterrupt:
        print("\n🛑 Examples interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error in examples: {e}")

if __name__ == "__main__":
    asyncio.run(main())