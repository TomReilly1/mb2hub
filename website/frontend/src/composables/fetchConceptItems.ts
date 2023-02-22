export default async function fetchConceptId(concept: string, idList: string[]) {
    try {
        let url: string = `${import.meta.env.VITE_API_URL}/${concept}/multiple?`
        for (let i = 0; i < idList.length; i++) {
            url += `${i}=${idList[i]}&`
        }
        url = url.slice(0, -1)
        console.log(url)
        const response: Response = await fetch(url)


        if (response.ok) {
            const data = await response.json()
            console.log(data)
            return data
        } else {
            throw Error('Network response was not ok.')
        }
    } catch (error) {
        return error
    }
}

