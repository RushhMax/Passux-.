export default async function apiFetch(
    endpoint, 
    { method, headers, body } = {}
  ) {
    //BASE_URI = "http://127.0.0.1:5000/"
    // const token = sessionStorage.getItem(tokenKey);
    const token = "EJiJsa3X25gDSNCPZDNfSPsq";
  
    if (token) {
      headers = {
        Authorization: `Token token=${token}`,
        ...headers,
      };
    }
  
    if (body) {
      headers = {
        "Content-Type": "application/json",
        ...headers,
      };
    }
  
    const config = {
      method: method || (body ? "POST" : "GET"),
      headers,
      body: body ? JSON.stringify(body) : null,
    };
  
    const response = await fetch(`http://127.0.0.1:5000/api/${endpoint}/`, config);
  
    let data;
    if (!response.ok) {
      try {
        data = await response.json();
      } catch (error) {
        throw new Error(response.statusText);
      }
      throw new Error(data.errors);
    }
  
    try {
      data = await response.json();
    } catch (error) {
      data = response.statusText;
    }
  
    return data;
  }
  
