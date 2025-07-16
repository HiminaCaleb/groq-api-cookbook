"""
Test script for AI Pricing Agent functionality

This script tests the core functionality of the pricing agent
without requiring real API keys or full browser installation.
"""

import asyncio
import json
import os
from pricing_agent import PricingAgent, get_pricing_data

async def test_validation():
    """Test input validation functionality"""
    print("🧪 Testing Input Validation")
    print("-" * 30)
    
    # Set a test API key to allow initialization
    os.environ['GROQ_API_KEY'] = 'test_key_for_validation'
    
    agent = PricingAgent()
    
    # Test valid items
    valid_items = agent.validate_items(['laptop', 'headphones', 'phone'])
    assert len(valid_items) == 3
    print(f"✅ Valid items test passed: {valid_items}")
    
    # Test mixed valid/invalid items
    mixed_items = agent.validate_items(['laptop', '', '   ', 'phone'])
    assert len(mixed_items) == 2
    print(f"✅ Mixed items test passed: {mixed_items}")
    
    # Test error cases
    try:
        agent.validate_items([])
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✅ Empty list validation test passed")
    
    try:
        agent.validate_items("not a list")
        assert False, "Should have raised ValueError" 
    except ValueError:
        print("✅ Invalid type validation test passed")

async def test_data_structures():
    """Test data structure creation and serialization"""
    print("\n🧪 Testing Data Structures")
    print("-" * 30)
    
    from pricing_agent import PriceData, ShopSource
    
    # Test ShopSource
    shop = ShopSource("TestShop", "https://test.com", "/search?q={item}")
    assert shop.name == "TestShop"
    print("✅ ShopSource creation test passed")
    
    # Test PriceData
    price_data = PriceData(
        item_name="test_item",
        shop_name="test_shop", 
        price=29.99,
        currency="USD",
        availability="in_stock",
        url="https://test.com",
        timestamp="2024-01-01T00:00:00",
        confidence_score=0.95
    )
    
    # Test serialization
    data_dict = price_data.__dict__
    assert data_dict['price'] == 29.99
    print("✅ PriceData creation and serialization test passed")

async def test_components_initialization():
    """Test component initialization without real API calls"""
    print("\n🧪 Testing Component Initialization")
    print("-" * 30)
    
    from pricing_agent import ConfigManager, WebScraper, RetryHandler
    
    # Test ConfigManager with test key
    os.environ['GROQ_API_KEY'] = 'test_key'
    config = ConfigManager()
    assert config.groq_api_key == 'test_key'
    print("✅ ConfigManager test passed")
    
    # Test WebScraper initialization
    scraper = WebScraper()
    await scraper.initialize()  # Should work in simulation mode
    await scraper.cleanup()
    print("✅ WebScraper initialization test passed")
    
    # Test RetryHandler
    call_count = 0
    async def test_func():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise Exception("Test error")
        return "success"
    
    result = await RetryHandler.retry_with_backoff(test_func, max_retries=3, base_delay=0.1)
    assert result == "success"
    assert call_count == 2
    print("✅ RetryHandler test passed")

async def test_mock_pricing_flow():
    """Test the full pricing flow in simulation mode"""
    print("\n🧪 Testing Mock Pricing Flow")
    print("-" * 30)
    
    # Set test environment
    os.environ['GROQ_API_KEY'] = 'test_key'
    
    try:
        # This will use simulation mode for all components
        result = await get_pricing_data(['test_laptop'])
        
        # Verify structure
        assert 'status' in result
        assert 'data' in result
        assert result['status'] == 'success'
        assert result['items_requested'] == 1
        
        print(f"✅ Mock pricing flow test passed")
        print(f"   Items requested: {result['items_requested']}")
        print(f"   Prices found: {result['prices_found']}")
        print(f"   Execution time: {result['execution_time_seconds']}s")
        
    except Exception as e:
        print(f"❌ Mock pricing flow test failed: {e}")
        raise

async def run_all_tests():
    """Run all tests"""
    print("🚀 Running AI Pricing Agent Tests")
    print("=" * 50)
    
    try:
        await test_validation()
        await test_data_structures()
        await test_components_initialization()
        await test_mock_pricing_flow()
        
        print("\n" + "=" * 50)
        print("🎉 All tests passed successfully!")
        print("The AI Pricing Agent implementation is working correctly.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(run_all_tests())