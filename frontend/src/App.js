import { useEffect, useState } from "react"
import "./App.css"
import axios from "axios"

const client = axios.create({
  baseURL: "http://localhost:8000/"
})

function App() {
  const [posts, setPosts] = useState([])
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")

  const fetchData = () => {
    client
      .get("api/posts/")
      .then((response) => {
        setPosts(response.data.posts)
      })
      .catch((err) => console.log(err))
  }
  useEffect(() => {
    fetchData()
  }, [])

  const handleFormSubmit = (e) => {
    e.preventDefault()
    console.log({ title, content })
    client
      .post("api/posts/", { title, content })
      .then(() => fetchData())
      .catch((err) => console.log(err))
    setTitle("")
    setContent("")
  }

  const handleDelete = (id) => {
    client
      .delete("api/posts/" + id)
      .then(() => fetchData())
      .catch((err) => console.log(err))
  }

  return (
    <>
      <h1>Hello World</h1>
      <ul>
        {posts?.map((post) => (
          <li key={post.id}>
            {post.title} - {post.content}{" "}
            <button onClick={() => handleDelete(post.id)}>delete</button>
          </li>
        ))}
      </ul>
      <form onSubmit={handleFormSubmit}>
        <label htmlFor="title">Title</label>
        <input
          type="text"
          name="title"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <label htmlFor="content">Content</label>
        <input
          type="text"
          name="content"
          id="content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
    </>
  )
}

export default App
