#!/usr/bin/env python3
"""
Simple Python application for Jenkins CI/CD demonstration
Author: Alex - DevOps Learning Journey
Date: October 2025
"""

def greet(name="World"):
    """
    Return a greeting message
    
    Args:
        name (str): Name to greet (default: "World")
    
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}! Welcome to Jenkins CI/CD!"

def add(a, b):
    """
    Add two numbers
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Sum of a and b
    """
    return a + b

def multiply(a, b):
    """
    Multiply two numbers
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Product of a and b
    """
    return a * b

def get_app_info():
    """
    Return application information
    
    Returns:
        dict: Application metadata
    """
    return {
        "name": "Jenkins Python Demo App",
        "version": "1.0.0",
        "author": "Alex",
        "description": "Learning DevOps with Jenkins"
    }

def main():
    """Main function - entry point"""
    print("=" * 50)
    print("🚀 Jenkins Python App - Running")
    print("=" * 50)
    
    # Display app info
    info = get_app_info()
    print(f"\n📦 App: {info['name']}")
    print(f"📌 Version: {info['version']}")
    print(f"👤 Author: {info['author']}")
    
    # Test functions
    print("\n🧪 Testing Functions:")
    print(f"  {greet('Alex')}")
    print(f"  2 + 3 = {add(2, 3)}")
    print(f"  4 × 5 = {multiply(4, 5)}")
    
    print("\n✅ Application is running successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()