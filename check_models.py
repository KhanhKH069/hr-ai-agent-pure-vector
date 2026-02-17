#!/usr/bin/env python3
"""Check Ollama Models - Offline Version"""

import subprocess
import sys

def check_ollama():
    """Check if Ollama is running and available models"""
    
    print("🔍 Checking Ollama installation...\n")
    
    # Check if ollama is installed
    try:
        result = subprocess.run(['ollama', '--version'], 
                              capture_output=True, 
                              text=True,
                              timeout=5)
        if result.returncode == 0:
            print(f"✅ Ollama installed: {result.stdout.strip()}\n")
        else:
            print("❌ Ollama not found. Install from: https://ollama.ai\n")
            return False
    except FileNotFoundError:
        print("❌ Ollama not found. Install from: https://ollama.ai")
        print("\nMac/Linux: curl https://ollama.ai/install.sh | sh")
        print("Windows: Download from ollama.ai\n")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  Ollama command timed out\n")
        return False
    
    # Check available models
    print("📦 Checking available models...\n")
    try:
        result = subprocess.run(['ollama', 'list'], 
                              capture_output=True, 
                              text=True,
                              timeout=10)
        
        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("Available models:")
                print(output)
                print()
                
                # Check for recommended models
                if 'llama3.2' in output:
                    print("✅ llama3.2 found (recommended for speed)")
                else:
                    print("⚠️  llama3.2 not found")
                    print("   Install: ollama pull llama3.2")
                
                if 'qwen2.5' in output:
                    print("✅ qwen2.5 found (better Vietnamese support)")
                else:
                    print("💡 For better Vietnamese: ollama pull qwen2.5")
                
            else:
                print("⚠️  No models installed")
                print("\nInstall a model:")
                print("  ollama pull llama3.2     # Fast (2GB)")
                print("  ollama pull qwen2.5:7b   # Better quality (4GB)")
                print("  ollama pull mistral      # Balanced (4GB)")
        else:
            print("❌ Error checking models")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⚠️  ollama list command timed out")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    # Check if Ollama server is running
    print("\n🔌 Checking Ollama server...")
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=3)
        if response.status_code == 200:
            print("✅ Ollama server is running on http://localhost:11434")
        else:
            print("⚠️  Ollama server responded with error")
    except:
        print("❌ Ollama server not running")
        print("\nStart server: ollama serve")
        print("(Run in separate terminal)\n")
        return False
    
    print("\n" + "="*50)
    print("✅ All checks passed! Ready to use offline!")
    print("="*50)
    return True

if __name__ == "__main__":
    success = check_ollama()
    sys.exit(0 if success else 1)
