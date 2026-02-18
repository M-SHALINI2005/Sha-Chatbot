import { useState } from "react";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [activeTab, setActiveTab] = useState("chat");
  const [lastJSON, setLastJSON] = useState(null);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const text = input;
    setInput("");

    
    setMessages(prev => [...prev, { sender:"user", text }]);

    const res = await fetch(`http://127.0.0.1:8000/chat?q=${input}`);
    const data = await res.json();
    
    setLastJSON(data);

    const botMsg = {
      sender: "bot",
      text: data.response,
      books: data.metadata
    };

    setMessages(prev => [...prev, botMsg]);
    setInput("");
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>📚 Book Chatbot Dashboard</h2>

      {/* Tabs */}
      <div style={styles.tabs}>
        <button
          style={activeTab === "chat" ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab("chat")}
        >
          Chat UI
        </button>

        <button
          style={activeTab === "json" ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab("json")}
        >
          JSON Output
        </button>
      </div>

      {/* Chat Tab */}
      {activeTab === "chat" && (
        <>
          <div style={styles.chatBox}>
            {messages.map((msg, i) => (
              <div key={i} style={msg.sender === "user" ? styles.user : styles.bot}>
                <p>{msg.text}</p>

                {msg.books && msg.books.map((b, i) => (
                  <div key={i} style={styles.card}>
                    <b>{b.title}</b><br/>
                    Author: {b.authors}<br/>
                    Rating: {b.average_rating}
                  </div>
                ))}
              </div>
            ))}
          </div>

          <div style={styles.inputBox}>
            <input
              value={input}
              onChange={e => setInput(e.target.value)}
              placeholder="Ask about books..."
              style={styles.input}
              onKeyDown={e => e.key === "Enter" && sendMessage()}
            />
            <button onClick={sendMessage} style={styles.btn}>Send</button>
          </div>
        </>
      )}

      {/* JSON TAB */}
      {activeTab === "json" && (
        <pre style={styles.jsonBox}>
          {lastJSON
            ? JSON.stringify(lastJSON, null, 2)
            : "No response yet. Ask a question first."}
        </pre>
      )}
    </div>
  );
}

const styles = {
  container: { width: "420px", margin: "40px auto", fontFamily: "sans-serif" },
  title: { textAlign: "center" },

  tabs: { display: "flex", marginBottom: "10px" },

  tab: {
    flex: 1,
    padding: "10px",
    background: "#eee",
    border: "none",
    cursor: "pointer"
  },

  activeTab: {
    flex: 1,
    padding: "10px",
    background: "#4CAF50",
    color: "white",
    border: "none",
    cursor: "pointer"
  },

  chatBox: {
    height: "400px",
    overflowY: "auto",
    border: "1px solid #ddd",
    padding: "10px",
    borderRadius: "10px"
  },

  user: {
    background: "#DCF8C6",
    padding: "10px",
    borderRadius: "10px",
    margin: "5px",
    textAlign: "right"
  },

  bot: {
    background: "#f1f1f1",
    padding: "10px",
    borderRadius: "10px",
    margin: "5px"
  },

  inputBox: { display: "flex", marginTop: "10px" },

  input: { flex: 1, padding: "10px" },

  btn: { padding: "10px 20px" },

  card: {
    background: "white",
    padding: "8px",
    marginTop: "5px",
    borderRadius: "6px",
    border: "1px solid #ddd"
  },

  jsonBox: {
    height: "450px",
    overflow: "auto",
    background: "#111",
    color: "#0f0",
    padding: "15px",
    borderRadius: "10px",
    fontSize: "14px"
  }
};
