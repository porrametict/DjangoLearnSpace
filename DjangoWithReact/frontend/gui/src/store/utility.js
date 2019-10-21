export const updateObject = (oldObject,updatedProportties) => {
    return {
        ...oldObject,
        ...updatedProportties
    }
}