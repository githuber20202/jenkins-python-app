#!/usr/bin/env python3
"""
Unit tests for app.py
"""

import sys
import app

def test_greet_default():
    """Test greet function with default parameter"""
    result = app.greet()
    assert "Hello, World!" in result, "Default greeting failed"
    print("✅ test_greet_default PASSED")
    return True

def test_greet_custom():
    """Test greet function with custom name"""
    result = app.greet("Alex")
    assert "Hello, Alex!" in result, "Custom greeting failed"
    print("✅ test_greet_custom PASSED")
    return True

def test_add():
    """Test add function"""
    assert app.add(2, 3) == 5, "2 + 3 should equal 5"
    assert app.add(-1, 1) == 0, "-1 + 1 should equal 0"
    assert app.add(0, 0) == 0, "0 + 0 should equal 0"
    assert app.add(100, 200) == 300, "100 + 200 should equal 300"
    print("✅ test_add PASSED")
    return True

def test_multiply():
    """Test multiply function"""
    assert app.multiply(2, 3) == 6, "2 × 3 should equal 6"
    assert app.multiply(-2, 3) == -6, "-2 × 3 should equal -6"
    assert app.multiply(0, 100) == 0, "0 × 100 should equal 0"
    assert app.multiply(5, 5) == 25, "5 × 5 should equal 25"
    print("✅ test_multiply PASSED")
    return True

def test_get_app_info():
    """Test get_app_info function"""
    info = app.get_app_info()
    assert "name" in info, "App info should contain 'name'"
    assert "version" in info, "App info should contain 'version'"
    assert "author" in info, "App info should contain 'author'"
    assert info["author"] == "Alex", "Author should be Alex"
    print("✅ test_get_app_info PASSED")
    return True

def run_all_tests():
    """Run all tests and report results"""
    print("=" * 50)
    print("🧪 Running Unit Tests")
    print("=" * 50)
    
    tests = [
        test_greet_default,
        test_greet_custom,
        test_add,
        test_multiply,
        test_get_app_info
    ]
    
    failed = 0
    passed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} ERROR: {e}")
            failed += 1
    
    print("=" * 50)
    print(f"📊 Test Results:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Total: {passed + failed}")
    print("=" * 50)
    
    if failed > 0:
        print("\n❌ TESTS FAILED!")
        sys.exit(1)
    else:
        print("\n🎉 ALL TESTS PASSED!")
        sys.exit(0)

if __name__ == "__main__":
    run_all_tests()
