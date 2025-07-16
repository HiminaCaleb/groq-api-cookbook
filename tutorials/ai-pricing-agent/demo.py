"""
Demo script for AI Pricing Agent with real Groq integration

This script demonstrates the full functionality of the pricing agent
when provided with actual API keys. It includes fallback modes when
keys are not available.
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from pricing_agent import get_pricing_data, PricingAgent

def check_api_keys():
    """Check which API keys are available"""
    groq_key = os.getenv('GROQ_API_KEY')
    mapbox_key = os.getenv('MAPBOX_API_KEY')
    
    print("🔐 API Key Status:")
    print(f"   GROQ_API_KEY: {'✅ Available' if groq_key else '❌ Missing'}")
    print(f"   MAPBOX_API_KEY: {'✅ Available' if mapbox_key else '❌ Missing (optional)'}")
    
    return bool(groq_key), bool(mapbox_key)

async def demo_with_real_apis():
    """Demonstration with real API integration"""
    print("🤖 AI Pricing Agent - Real API Demo")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Check API key availability
    has_groq, has_mapbox = check_api_keys()
    
    if not has_groq:
        print("\n⚠️ GROQ_API_KEY not found!")
        print("Please set your Groq API key to see full functionality.")
        print("Get a free key at: https://console.groq.com/")
        print("\nRunning in simulation mode...")
    
    print("\n" + "="*50)
    
    # Demo items for price collection
    demo_items = [
        "wireless bluetooth headphones",
        "laptop computer",
        "smartphone"
    ]
    
    print(f"🔍 Collecting prices for: {', '.join(demo_items)}")
    print("This will demonstrate:")
    print("   • Item validation and processing")
    print("   • Multi-shop concurrent scraping")
    print("   • AI-powered price extraction with Groq")
    print("   • Location data from Mapbox (if available)")
    print("   • Error handling and retry logic")
    print("   • Structured output with metadata")
    print()
    
    try:
        # Get pricing data
        result = await get_pricing_data(demo_items)
        
        # Display results
        print("✅ Price collection completed!")
        print(f"📊 Results Summary:")
        print(f"   • Items processed: {result['items_requested']}")
        print(f"   • Prices found: {result['prices_found']}")
        print(f"   • Shop sources: {result['shop_sources_used']}")
        print(f"   • Execution time: {result['execution_time_seconds']} seconds")
        print(f"   • Status: {result['status']}")
        
        # Show detailed price data
        if result['data']:
            print(f"\n📝 Detailed Price Data:")
            for i, price_data in enumerate(result['data'], 1):
                print(f"\n   Price Entry #{i}:")
                print(f"   📦 Item: {price_data['item_name']}")
                print(f"   🏪 Shop: {price_data['shop_name']}")
                print(f"   💰 Price: {price_data['currency']} {price_data['price']}")
                print(f"   📦 Availability: {price_data['availability']}")
                print(f"   🎯 Confidence: {price_data['confidence_score']:.2f}")
                print(f"   🕐 Timestamp: {price_data['timestamp']}")
                
                if price_data.get('location'):
                    location = price_data['location']
                    print(f"   📍 Location: {location.get('place_name', 'N/A')}")
                    if location.get('coordinates'):
                        coords = location['coordinates']
                        print(f"   🌍 Coordinates: {coords[1]:.4f}, {coords[0]:.4f}")
                else:
                    print(f"   📍 Location: Not available")
                
                print(f"   🔗 URL: {price_data['url']}")
        
        # Show raw JSON for developers
        print(f"\n🔧 Raw JSON Response (for developers):")
        print(json.dumps(result, indent=2))
        
        return result
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        print(f"This might be due to missing API keys or network issues.")
        return None

async def demo_error_scenarios():
    """Demonstrate error handling capabilities"""
    print("\n" + "="*50)
    print("🚨 Error Handling Demonstration")
    print("="*50)
    
    # Test different error scenarios
    error_tests = [
        ([], "Empty item list"),
        (["", "  ", "\t"], "All invalid items"),
        ("not_a_list", "Wrong data type"),
        (["valid_item"], "Valid case for comparison")
    ]
    
    for test_input, description in error_tests:
        print(f"\n🧪 Testing: {description}")
        print(f"   Input: {test_input}")
        
        try:
            result = await get_pricing_data(test_input)
            print(f"   ✅ Success: Found {result['prices_found']} prices")
        except Exception as e:
            print(f"   ❌ Expected error: {e}")

async def demo_performance():
    """Demonstrate performance characteristics"""
    print("\n" + "="*50)
    print("⚡ Performance Demonstration")
    print("="*50)
    
    # Test concurrent processing
    import time
    
    # Single item vs multiple items
    print("\n📈 Testing scalability:")
    
    test_cases = [
        (["single_item"], "Single item"),
        (["item1", "item2"], "Two items"),
        (["item1", "item2", "item3"], "Three items")
    ]
    
    for items, description in test_cases:
        print(f"\n🔍 {description}:")
        start_time = time.time()
        
        try:
            result = await get_pricing_data(items)
            end_time = time.time()
            
            print(f"   ⏱️ Time: {end_time - start_time:.2f}s")
            print(f"   📊 Prices: {result['prices_found']}")
            print(f"   🏪 Shops: {result['shop_sources_used']}")
            print(f"   📈 Rate: {result['prices_found']/(end_time - start_time):.1f} prices/sec")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")

async def main():
    """Main demo function"""
    print("🚀 AI Pricing Agent - Complete Demonstration")
    print("This demo showcases all features of the pricing agent.")
    print("Note: Some features require valid API keys to work fully.")
    
    try:
        # Main functionality demo
        result = await demo_with_real_apis()
        
        # Error handling demo
        await demo_error_scenarios()
        
        # Performance demo
        await demo_performance()
        
        print("\n" + "="*70)
        print("🎉 Demo completed successfully!")
        
        if result:
            print(f"✅ The AI Pricing Agent is working correctly.")
            print(f"📊 Last run found {result['prices_found']} prices in {result['execution_time_seconds']}s")
        
        print(f"\n📚 Next steps:")
        print(f"   • Set GROQ_API_KEY for full AI functionality")
        print(f"   • Set MAPBOX_API_KEY for location features")
        print(f"   • Run 'playwright install' for real browser automation")
        print(f"   • Check README.md for detailed documentation")
        print(f"   • Explore the Jupyter notebook for interactive examples")
        
    except KeyboardInterrupt:
        print("\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(main())