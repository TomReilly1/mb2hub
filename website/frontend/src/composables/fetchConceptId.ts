export default async function fetchConceptId(concept: string, id: string) {
    try {
        const url: string = `${import.meta.env.VITE_API_URL}/${concept}/${id}`
        const response: Response = await fetch(url)

        if (response.ok) {
            const data = await response.json()
            return data
        } else {
            throw new Error('Network response was not ok.')
        }
    } catch (error) {
        return error
    }
}